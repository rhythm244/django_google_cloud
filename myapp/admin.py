from django.contrib import admin
from .models import Employee, Division, Position, Rank, Airport, Flight, Picture, Lessonlearn


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id",'rank','first_name_thai','last_name_thai','position','afaps','date_birth', 'update')

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'department') 

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'position') 

class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'icao_code', 'city', 'update') 

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration') 

class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'employee_image')

class LessonlearnAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_fly','update')


admin.site.register(Division, DivisionAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Rank)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Lessonlearn, LessonlearnAdmin)

