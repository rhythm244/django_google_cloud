from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
from .form import PictureForm, EmployeeForm, LessonlearnForm
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
    # employees = Employee.objects.filter(is_pilot=True).order_by('lucky_number')
    employees = []
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

        #จัดเตรียมข้อมูลเอาไว้ใช้ด้านล่าง ไม่รู้ทำไมใช้ employee. เลยไม่ได้ เลยต้องใส่ตัวแปรเพิ่ม
        telephone_already = employee.telephone
        rank_already = employee.rank
        firstnamethai_already = employee.first_name_thai
        lastnamethai_already = employee.last_name_thai
        firstnameeng_already = employee.first_name_eng
        lastnameeng_already = employee.last_name_eng
        position_already = employee.position
        position_other_already = employee.position_other
        
        form = EmployeeForm(request.POST, instance=employee)
        
        if form.is_valid():
            f = form.save(commit=False)
            f.employee_id = employee_id #ต้องมีบรรทัดนี้ เพราะถ้าไม่ใส่มันจะไม่รู้ว่าเป็นของ pk ไหน

            #ถ้ามีข้อมูลเก่าอยู่แล้ว ให้นำข้อมูลเก่ามาใส่ ถ้า user ใส่ None มาใน Form
            if f.rank == None:
                f.rank = rank_already
            if f.first_name_thai == None:
                f.first_name_thai = firstnamethai_already
            if f.last_name_thai == None:
                f.last_name_thai = lastnamethai_already
            if f.first_name_eng == None:
                f.first_name_eng = firstnameeng_already
            if f.last_name_eng == None:
                f.last_name_eng = lastnameeng_already
            if f.telephone == None:
                f.telephone = telephone_already
            if f.position == None:
                f.position = position_already

            # hide ไว้ เพราะถ้าไม่ใส่คือไม่มีอยู่แล้ว
            # if f.position_other == None:
            #     f.position_other = position_other_already

            f.save()        
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

@login_required
def lessonlearn(request):
    if request.method == 'GET':
        lesson = Lessonlearn.objects.all().order_by('-date_fly')
        context = {
            'lessons': lesson,
        }
        return render(request, 'myapp/lessonlearn.html',context)

@login_required
def lessonlearn_form(request):
    if request.method == 'GET':
        form = LessonlearnForm()
        context = {
            'form': form,
        }
        return render(request, 'myapp/lessonlearn_form.html',context)

    elif request.method == 'POST':
        form = LessonlearnForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("myapp:lessonlearn"))

@login_required
def lessonlearn_info(request, id):
    lessonlearn = Lessonlearn.objects.filter(pk=id)

    context = {
        'lessons': lessonlearn,
    }
    
    return render(request, 'myapp/lessonlearn_one.html',context)
    
        