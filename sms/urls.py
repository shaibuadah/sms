from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='homepage' ),

    # ========== Super-Admin URL Patterns ========== #
    path('admin_dashboard', views.admin_dashboard, name="admin-dashboard"),
    path('admin_manage_school', views.admin_manage, name="admin-school"),
    path('admin_allschool', views.admin_view_AllSchools, name="admin-view-allschool"),
    path('<int:school_id>/', views.admin_viewschool_detail, name='admin-viewschool-detail'),
    path('<int:school_id>/#delete', views.School_Delete, name='school-delete'),

    path('registerSchool/', views.registerSchool, name='registerSchool'),

    # ========== School URL Patterns ========== #
    path('school_dashboard', views.schooldashboard, name="school-dashboard"),

    # ========== Department URL Patterns ========== #
    path('department_dashboard', views.deptdashboard, name="department-dashboard"),

    
    
]