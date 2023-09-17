from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.schoolProfile, name='schoolProfile'),

    path('admin_addSchool/', views.admin_addSchool, name='admin-AddSchool'),
    path('allSchools/', views.admin_view_AllSchools, name='admin-view-AllSchools'),
    path('school/<slug:school_slug>/', views.admin_viewschool_detail, name='admin_viewschool_detail'),
    path('approveSchools/', views.admin_Approve_AllSchools, name='admin-approve-Schools'),
    path('school/departments/<int:pk>/', views.admin_view_department, name='admin_view_department'),
    path('school/students/<int:pk>/', views.admin_students_by_school, name='admin_students_by_school'),
    path('school/department/<int:pk>/', views.admin_students_by_department, name='admin_students_by_category'),

    path('delete/<slug:school_slug>/', views.admin_School_Delete, name='admin-school-delete'),
    path('allStudents/', views.admin_view_students, name='admin-view-allStudents'),

]