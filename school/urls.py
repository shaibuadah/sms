from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.schoolProfile, name='schoolProfile'),

    path('admin_addSchool/', views.admin_addSchool, name='admin-AddSchool'),
    path('admin/allSchools/', views.admin_view_AllSchools, name='admin-view-AllSchools'),
    path('school/<slug:school_slug>/', views.admin_viewschool_detail, name='admin_viewschool_detail'),
    path('approveSchools/', views.admin_Approve_AllSchools, name='admin-approve-Schools'),
    path('school/departments/<int:pk>/', views.admin_view_department, name='admin_view_department'),
    path('school/students/<int:pk>/', views.admin_students_by_school, name='admin_students_by_school'),
    path('school/department/<int:pk>/', views.admin_students_by_department, name='admin_students_by_category'),

    path('delete/<slug:school_slug>/', views.admin_School_Delete, name='admin-school-delete'),
    path('allStudents/', views.admin_view_students, name='admin-view-allStudents'),
    path('studentdue4payment/', views.admin_view_studentsdue4payment, name='adminview-studentdue4payment'),
    path('send_paymentconfirmation/', views.send_paymentconfirmationtostudent, name='send-paymentconfirmation'),

    # ====== SCHOOL URLS ====== #
    path('Add_Dept', views.school_addDept, name='addDept'),
    path('view_allDept', views.schoolview_allDept, name='view_allDept'),
    path('<slug:dept_slug>', views.school_viewsdepartment_detail, name='view-Deptdetails'),
    path('delete/<slug:dept_slug>/', views.SchoolDelete_department, name='school-delete-department'),
    path('allStudents/', views.schoolview_allStudent, name='school-view-allStudents'),

]