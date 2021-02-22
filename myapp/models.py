from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from PIL import Image
# from myapp.storage import OverwriteStorage


# Create your models here.

# class User(AbstractUser):
#     pass

class Airport(models.Model):
    icao_code = models.CharField(max_length=4, null=False, blank=False) #valid upper case ENG alphabet
    city = models.CharField(max_length=30, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    runway_length = models.IntegerField(null=False)
    runway_direction = models.CharField(max_length=30,  null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.icao_code} {self.city} ({self.country} {self.update})"

class Flight(models.Model):
    
    origin = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name="arivals")
    duration = models.IntegerField(help_text='duration in minute')

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
    
    airforce_rank = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.airforce_rank}"

class Picture(models.Model):
    class Meta():
        ordering = ['id']
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, default=None, null=False, related_name='employee_picture')
    employee_image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f"{self.employee.rank} {self.employee.first_name_thai} {self.employee_image}"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.employee_image.path)

    #     if img.height > 100 or img.width > 100:
    #         output_size = (100, 100)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class Employee(models.Model):
    
    class Meta():
        ordering = ['id']

    first_name_eng = models.CharField(max_length=64, blank=True, null=True)
    last_name_eng = models.CharField(max_length=64, blank=True, null=True)
    first_name_thai = models.CharField(max_length=64, blank=True, null=True)
    last_name_thai = models.CharField(max_length=64, blank=True, null=True)
    date_birth = models.DateField(default=None)

    line_id = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=10, help_text='fill 10 number', blank=True, null=True)
    email = models.EmailField(unique=True)
    picture = models.ForeignKey('Picture', on_delete=models.SET_NULL, related_name='employee_picture', blank=True, null=True)

    division = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='employee_division', blank=True, null=True)
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='rank', blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='employee_position', blank=True, null=True)
    lucky_number = models.DecimalField(max_digits=4,decimal_places=0, blank=True, null=True)
    afaps = models.IntegerField(default=None)

    passport = models.CharField(max_length=9, default=None, blank=True, null=True)
    visa = models.CharField(max_length=14, default=None, blank=True, null=True)

    still_service = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.first_name_thai} {self.division} {self.position}"