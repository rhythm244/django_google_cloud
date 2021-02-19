from django.contrib import admin
from .models import Employee, Division, Position, Rank

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    pass
    # list_display = ("id")

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'department') 

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'position') 


admin.site.register(Division, DivisionAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Rank)
admin.site.register(Employee, EmployeeAdmin)

