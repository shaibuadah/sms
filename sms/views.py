from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import SchoolSms, Department, Student
from authentication.views import check_role_school, check_role_dept


from . import models




# Create your views here.

# Get Current Logedin School
def get_school(request):
    school = SchoolSms.objects.get(user=request.user)
    return school


# Get Current Logedin Department of a School
def get_department(request):
    department = Department.objects.get(user=request.user)
    return department

# ========== School Dashboard Function ========== #
@login_required(login_url='login')
@user_passes_test(check_role_school)
def schooldashboard(request):
    school = get_school(request)
    students = Student.objects.filter(school=school)
    context = {
        'school':school,
        'students':students,
    }
    return render(request, 'sms/school_dashboard.html', context)

# ========== Department Dashboard Function ========== #
@login_required(login_url='login')
@user_passes_test(check_role_dept)
def deptdashboard(request):
    department = get_department(request)
    students = Student.objects.filter(department=department)
    context = {
        'students': students,
        'department': department,
    }
    return render(request, 'sms/department_dashboard.html', context)


def home_view(request):
    if request.user.is_authenticated:
        pass
    return render(request,'sms/index.html')


def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'sms/admin_dashboard.html')
    
def admin_school(request):
    if request.user.is_authenticated:
        return render(request, 'sms/admin_school.html')
    
def admin_department(request):
    if request.user.is_authenticated:
        return render(request, 'sms/admin_department.html')
    

#for dashboard of adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

@login_required(login_url='login')
# @user_passes_test(is_admin)
def admin_dashboard_view(request):
    schoolcount=models.SchoolSms.objects.all().filter(status=True).count()
    pendingschoolcount=models.SchoolSms.objects.all().filter(status=False).count()

    departmentcount=models.Department.objects.all().filter(status=True).count()
    pendingdepartmentcount=models.Department.objects.all().filter(status=False).count()

    #aggregate function return dictionary so fetch data from dictionay
    mydict={
        'schoolcount':schoolcount,
        'pendingschoolcount':pendingschoolcount,

        'departmentcount':departmentcount,
        'pendingdepartmentcount':pendingdepartmentcount,

    }

    return render(request,'school/admin_dashboard.html',context=mydict)
