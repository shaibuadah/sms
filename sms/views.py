from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Count

from .models import SchoolSms, Department, Student
from authentication.views import check_role_school, check_role_dept, detectuser
from authentication.forms import UserForm
from authentication.models import CustomUser
from .forms import SchoolSmsForm, DepartmentForm


# Get Current Logedin School
def get_school(request):
    school = SchoolSms.objects.get(user=request.user)
    return school


# Get Current Logedin Department of a School
def get_department(request):
    department = Department.objects.get(user=request.user)
    return department



def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        redirectUrl = detectuser(user)
        return redirect(redirectUrl)
    return render(request,'sms/index.html')


# ======================================================================================= #
# ============================== SUPER ADMIN VIEW FUCTIONS ============================== #
# ======================================================================================= #

# ========== Super-Admin Dashboard ========== #
@login_required(login_url='login')
def admin_dashboard(request):
    schoolcount = SchoolSms.objects.all().count()
    allstudent = Student.objects.all().count()
    pendingschoolcount = SchoolSms.objects.all().count()

    mydict={
        'schoolcount':schoolcount,
        'allstudent': allstudent,
        'pendingschoolcount':pendingschoolcount,
    }
    return render(request,'sms/admin_dashboard.html',context=mydict)



# ========== Super-Admin Manage School ========== #
@login_required(login_url='login')
def admin_manage(request):
    if request.user.is_authenticated:
        return render(request, 'sms/admin_school.html')
    


# ========== Super-Admin View all Schools ========== #
@login_required(login_url='login')
def admin_view_AllSchools(request):
    all_schools = SchoolSms.objects.annotate(no_of_department=Count('departments'), no_of_students=Count('student'))
    mydict={
        'all_schools': all_schools,
    }
    return render(request,'sms/admin_view_allschool.html',context=mydict)



# ========== Super-Admin Add School ========== #
@login_required(login_url='login')
def registerSchool(request):

    user_form = UserForm(request.POST)
    school_form = SchoolSmsForm(request.POST)
    context = {
        'user_form': user_form,
        'school_form': school_form,
    }
    if request.method != 'POST':
        return render(request, 'sms/admin_add_school.html', context=context)
    
    elif request.method == 'POST':
        if user_form.is_valid() and school_form.is_valid:
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = CustomUser.SCHOOL
            user.save()

            school = school_form.save(commit=False)
            school.user = user
            school_name = school_form.cleaned_data['school_name']
            address = school_form.cleaned_data['address']
            mobile = school_form.cleaned_data['mobile']
            email = user_form.cleaned_data['email']
            school.save()

            # messages.success(request, 'Your account has been registered sucessfully! Please wait for the approval.')
            return redirect('admin-view-allschools')
        else:
            print('invalid form')
            print(user_form.errors)
    else:
        user_form = UserForm()
        school_form = SchoolSmsForm()

    return render(request, 'sms/admin_add_school.html', context)



# ========== Super-Admin View School Detail ========== #
@login_required(login_url='login')
def admin_viewschool_detail(request, id):
    school = get_object_or_404(SchoolSms, id=id)
    school_departments = Department.objects.filter(school=school).annotate(no_of_students=Count('student_department'))

    departments = Department.objects.filter(school=school).count()
    students = Student.objects.filter(school=school).count()

    user_form = UserForm(request.POST)
    department_form = DepartmentForm(request.POST)
    context = {
        'school': school,
        'school_departments': school_departments,
        'students': students,
        'departments': departments,

        'user_form': user_form,
        'department_form': department_form,
    }

    if request.method != 'POST':
        return render(request, 'sms/admin_viewschool_detail.html', context=context)
    
    elif request.method == 'POST':
        if user_form.is_valid() and department_form.is_valid:
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.is_HOD = True
            user.save()

            department = department_form.save(commit=False)
            department.user = user
            department.school = school
            dept_name = department_form.cleaned_data['dept_name']
            dept_code = department_form.cleaned_data['dept_code']
            email = user_form.cleaned_data['email']
            department.save()

            # messages.success(request, 'Your account has been registered sucessfully! Please wait for the approval.')
            return redirect('admin-viewschool-detail', id = id)
        else:
            print('invalid form')
            print(user_form.errors)
    else:
        user_form = UserForm()
        department_form = DepartmentForm()

    return render(request, 'sms/admin_viewschool_detail.html', context)

# ========== Super-Admin view particular school student ========== #
@login_required(login_url='login')
def adminview_singleschool_student(request, id):
    school = get_object_or_404(SchoolSms, id=id)
    school_student = Student.objects.filter(school=school)
    mydict={
        'school': school,
        'school_student': school_student,
    }
    return render(request, 'sms/adminview_singleschool_student.html', context=mydict)

# ========== Super-Admin Edit School ========== #
@login_required(login_url='login')
def admin_School_Edit(request, id):
    school = get_object_or_404(SchoolSms, id=id)
    
    user_detail = school.user
    context = {
        'user_values': user_detail,
        'school_values': school
    }
    if request.method == "GET":
        return render(request, 'sms/admin_edit_school.html', context)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        school_name = request.POST['school_name']
        address = request.POST['address']
        mobile = request.POST['mobile']
        
        user_detail.first_name = first_name
        user_detail.last_name = last_name
        user_detail.username = username
        user_detail.email  = email
        school.school_name = school_name
        school.address = address
        school.mobile = mobile

        user_detail.save()
        school.save()

        return redirect('admin-viewschool-detail', id=id)
 

    
    
    # messages.success(request, 'School Edited successfuly')
    # return redirect('admin-view-allschool')
    return render(request, 'sms/admin_edit_school.html', context)

# ========== Super-Admin Delete School ========== #
@login_required(login_url='login')
def admin_School_Delete(request, id):
    school = get_object_or_404(SchoolSms, id=id)
    user = CustomUser.objects.get(email = school.email)
    school.delete()
    user.delete()
    # messages.success(request, 'School Deleted')
    return redirect('admin-view-allschool')



# ========== Super-Admin Manage Departments ========== #
@login_required(login_url='login')  
def admin_view_allstudents(request):
    if request.user.is_authenticated:
        all_student = Student.objects.all()
        mydict = {
            'all_student': all_student
        }
        return render(request, 'sms/admin_view_allstudents.html', context=mydict)
    





# ======================================================================================= #
# ================================= SCHOOL VIEW FUCTIONS ================================= #
# ======================================================================================= #

# ========== School Dashboard ========== #
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



# ======================================================================================= #
# ============================== DEPARTMENT VIEW FUCTIONS ============================== #
# ======================================================================================= #

# ========== Department Dashboard ========== #
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