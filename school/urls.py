from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.schoolProfile, name='schoolProfile'),

    path('admin_addSchool/', views.admin_addSchool, name='admin-AddSchool'),
    path('admin/allSchools/', views.admin_view_AllSchools, name='admin-view-AllSchools'),
    path('school/<int:id>/', views.admin_viewschool_detail, name='admin_viewschool_detail'),
    path('admin/edit/<int:pk>/school/', views.admin_edit_school, name='edit_school'),
    path('school/departments/<int:pk>/', views.admin_view_department, name='admin_view_department'),
    path('school/students/<int:pk>/', views.admin_students_by_school, name='admin_students_by_school'),
    path('school/department/<int:pk>/', views.admin_students_by_department, name='admin_students_by_category'),

    path('delete/<int:id>/', views.admin_School_Delete, name='admin-school-delete'),
    path('allStudents/', views.admin_view_students, name='admin-view-allStudents'),
    path('studentdue4payment/', views.admin_view_studentsdue4payment, name='adminview-studentdue4payment'),
    path('send_paymentconfirmation/', views.send_paymentconfirmationtostudent, name='send-paymentconfirmation'),

    # ====== SCHOOL URLS ====== #
    path('Add_Dept', views.school_addDept, name='addDept'),
    path('view_allDept', views.schoolview_allDept, name='view_allDept'),
    path('<int:id>', views.school_viewsdepartment_detail, name='view-Deptdetails'),
    path('department/edit/<int:pk>/', views.edit_Department, name='edit_department'),
    path('school_delete/<int:id>/', views.SchoolDelete_department, name='school-delete-department'),
    path('school_view/allStudents/', views.schoolview_allStudent, name='school-view-allStudents'),
    # path('department/deptchange-password/', login_required(SchoolChangePasswordView.as_view(), login_url='/login/'), name='Deptchange-password'),


    # ================== DEPARTMENT URLS ================== #
    path('department/addstudent/', views.dept_addstudent, name='department-addStudents'),
    path('department_view/allStudents/', views.deptview_allstudents, name='departmentview-allStudents'),
    path('department/<int:pk>', views.deptview_studentdetail, name='deptview-studentdetails'),
    path('dept_delete/<int:pk>/student/', views.deptDelete_student, name='department-delete-student'),
    path('department_edit/<int:pk>student/', views.deptedit_student, name='dept-editstudent'),


    path('department/profile/', views.departmentProfile, name='departmentProfile'),
    
  
]