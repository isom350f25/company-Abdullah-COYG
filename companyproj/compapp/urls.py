from django.contrib import admin
from django.urls import path
from compapp.views import employee_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', employee_list_view, name="Employee_List")
]
