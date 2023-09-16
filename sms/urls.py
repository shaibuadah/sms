from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='homepage' ),

    # ========== Super-Admin URL Patterns ========== #
    path('admin_dashboard', views.admin_dashboard, name="admin-dashboard"),
    path('admin_manage_school', views.admin_manage, name="admin-school"),
    path('admin_allschool', views.admin_view_AllSchools, name="admin-view-allschool"),
    path('<str:id>', views.admin_viewschool_detail, name='admin-viewschool-detail'),
    path('<str:id>/admin_edit_school/', views.admin_School_Edit, name="admin-edit-school"),
    path('<str:id>/delete', views.admin_School_Delete, name='admin-school-delete'),
    path('admin_view_allstudents/', views.admin_view_allstudents, name="admin-view-allstudents"),
    path('adminview_singleschool_student/<str:id>', views.adminview_singleschool_student, name="adminview-singleschool-student"),

    path('registerSchool/', views.registerSchool, name='registerSchool'),

    # ========== School URL Patterns ========== #
    path('school_dashboard/', views.schooldashboard, name="school-dashboard"),

    # ========== Department URL Patterns ========== #
    path('department_dashboard/', views.deptdashboard, name="department-dashboard"),

    
    
]