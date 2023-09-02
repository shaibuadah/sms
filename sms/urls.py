from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='homepage' ),


   # path('admin_dashboard', views.admin_dashboard, name="admin-dashboard"),
    path('school_dashboard', views.schoolDashboard, name="school-dashboard"),
    path('department_dashboard', views.deptDashboard, name="department-dashboard"),
    
]
