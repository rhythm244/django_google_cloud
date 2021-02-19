from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

# class User(AbstractUser):
#     pass

class Division(models.Model):
    class Meta():
        ordering = ['id']
    department = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"{self.department}"

class Position(models.Model):
    class Meta():
        ordering = ['id']

    department = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='department_position', blank=False, null=False, default=None)
    position = models.CharField(max_length=50, default=None)

    def __str__(self):
        return f"{self.department} {self.position}"

class Rank(models.Model):
    class Meta():
        
        ordering = ['id']
    
    airforce_rank = models.CharField(max_length=6, null=False, blank=False)

    def __str__(self):
        return f"{self.department} {self.position}"

class Employee(models.Model):
    
    class Meta():
        ordering = ['id']

    first_name_eng = models.CharField(max_length=64, blank=True, null=True)
    first_name_thai = models.CharField(max_length=64, blank=True, null=True)
    last_name_eng = models.CharField(max_length=64, blank=True, null=True)
    last_name_thai = models.CharField(max_length=64, blank=True, null=True)
    date_birth = models.DateField(default=None)

    line_id = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=10, help_text='fill 10 number', blank=True, null=True)
    email = models.EmailField(unique=True)
    picture = models.ImageField() 

    division = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='employee_division', blank=True, null=True)
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='rank', blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='employee_position', blank=True, null=True)
    lucky_number = models.CharField(max_length=9, default=None, blank=True, null=True)

    passport = models.CharField(max_length=9, default=None, blank=True, null=True)
    visa = models.CharField(max_length=14, default=None, blank=True, null=True)

    still_service = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.first_name_thai} {self.division} {self.position}"