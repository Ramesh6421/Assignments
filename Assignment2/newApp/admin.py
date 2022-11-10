from django.contrib import admin
from newApp.models import Passenger
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['firstName']

admin.site.register(Passenger,EmployeeAdmin)
