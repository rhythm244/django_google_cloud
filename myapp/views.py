from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
from .form import PictureForm
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
        
def person(request):
    """แสดงคนของ ฝูง.601 ทั้งหมด """
    employees = Employee.objects.all()
    divisions = Division.objects.all()

    form = PictureForm()
  
    context = {
        'employees': employees, 
        'divisions': divisions,
        'form': form,
    }
    return render(request, "myapp/person.html", context)

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

def person_one(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    form = PictureForm()

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'myapp/person_one.html', context)

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

            return HttpResponseRedirect(reverse("myapp:index"))
    else: 
        form = PictureForm()
        context = {
            'form': form,
        }
        return render(request, 'myapp/index.html', context)
