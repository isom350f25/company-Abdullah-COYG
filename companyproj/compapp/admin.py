from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'joined_on', 'phone_number')
    search_fields = ('name','position')
    list_filter = ('joined_on',)
    pass
# Register your models here.
