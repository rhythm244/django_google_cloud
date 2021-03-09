from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
from .form import PictureForm, EmployeeForm
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == "GET":
        form = PictureForm()
        context = {
            'form': form,
        }
        return render(request, "myapp/index.html", context)

def login_view(request):  
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, "Log in Successed Let Go !")
            return HttpResponseRedirect(reverse("myapp:index"))
        else:
            return render(request, "myapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "myapp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("myapp:index"))

@login_required
def person(request):
    """ส่งแค่ division ไปเพื่อใช้ในการกด ของ user เอา เพราะถ้าส่งไปหมดจะ load ช้าเกิน """
    
    # employees = Employee.objects.order_by('afaps')
    divisions = Division.objects.all()

    form = PictureForm()
  
    context = {
        # 'employees': employees, 
        'divisions': divisions,
        'form': form,
    }
    return render(request, "myapp/person.html", context)

@login_required
def pilot_c130(request):
    """แสดงนักบิน C130 ที่ผ่านมาทุกคน """
    employees = Employee.objects.filter(is_pilot=True).order_by('lucky_number')
  
    context = {
        'employees': employees, 
    }
    return render(request, "myapp/pilot_c130.html", context)

@login_required
def person_division(request, division_id):
    """ทำเพื่อให้ filter ฝ่ายของฝูง.601 """
    employees = Employee.objects.filter(division_id=division_id)
    divisions = Division.objects.all()
    form = PictureForm()
  
    context = {
        'employees': employees, 
        'divisions': divisions,
        'form': form,
    }
    return render(request, "myapp/person.html", context)

@login_required
def person_one(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    form = PictureForm()
    form_employee = EmployeeForm()

    context = {
        'employee': employee,
        'form': form,
        'form_employee': form_employee, 
    }
    return render(request, 'myapp/person_one.html', context)

@login_required
def upload(request, employee_id):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.employee_id = employee_id
            # pic_em = f.pk
            f.save()
            
            #ลบรูปอื่นออกให้หมด ยกเว้นรูปล่าสุด
            Picture.objects.filter(employee_id=employee_id , id__lt=int(f.id)).delete()

            employee = Employee.objects.filter(pk=employee_id)
            employee_picture = form.cleaned_data['employee_image']

            for item in employee:
                item.picture = f
                item.id = employee_id
                item.save()          
                messages.success(request, "Upload Success")
        else:
            messages.error(request, "File not more than 500 Kb")

        return HttpResponseRedirect(reverse("myapp:person_one", args=(employee_id,)))
    else: 
        form = PictureForm()
        context = {
            'form': form,
        }
        return render(request, 'myapp/index.html', context)

@login_required
def upload_employee(request, employee_id):
    if request.method == 'POST':

        employee = Employee.objects.filter(pk=employee_id).first()

        form = EmployeeForm(request.POST, instance=employee)
        
        if form.is_valid():

            form.save()
            # employee.id = employee_id
            # employee.save()          
            messages.success(request, "Edit Success")
        else:
            messages.error(request, "Error")

        return HttpResponseRedirect(reverse("myapp:person_one", args=(employee_id,)))
    else: 
        form = PictureForm()
        context = {
            'form': form,
        }
        return render(request, 'myapp/index.html', context)