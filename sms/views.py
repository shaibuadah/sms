from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import SchoolSession, SchoolSms, Department, Student
from authentication.views import check_role_school, check_role_dept




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