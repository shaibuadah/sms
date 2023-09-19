from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.template.defaultfilters import slugify
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template

from authentication.forms import UserForm, UserInfoForm
from authentication.models import CustomUser
from authentication.views import check_role_superuser, check_role_school, check_role_dept

from .models import School, Department, Student
from .forms import SchoolForm, SchoolInfoForm, DeptForm, DeptInfoForm





# Get Current Logedin School
def get_school(request):
    school = School.objects.get(user=request.user)
    return school


# Get Current Logedin School
def get_department(request):
    department = Department.objects.get(user=request.user)
    return department


# SCHOOL PROFILE
@login_required(login_url='login')
@user_passes_test(check_role_school)
def schoolProfile(request):
    profile = request.user
    school = get_object_or_404(School, user=request.user)

    if request.method == 'POST':
        form = SchoolInfoForm(request.POST, instance=profile)
        school_form = SchoolForm(request.POST, instance=school)
        if form.is_valid() and school_form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.POST['school_name']
            obj.save()
            school_form.save()
            messages.success(request, 'School info updated successfully.')
            return redirect('schoolProfile')
        else:
            messages.error(request, 'Something Went Wrong.')
            print(form.errors)
            print(school_form.errors)
    else:
        form = SchoolInfoForm(instance = profile)
        school_form = SchoolForm(instance=school)

    context = {
        'form': form,
        'school_form': school_form,
        'profile': profile,
        'school': school,
    }
    return render(request, 'school/schoolProfile.html', context)


# ========== Super-Admin Add Schools ========== #
@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_addSchool(request):
    if request.method == 'POST':
        # store the data and create the user
        form = UserForm(request.POST)
        school_form = SchoolForm(request.POST)       
        if form.is_valid() and school_form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(name=name,
                                            username=username, 
                                            email=email,
                                            password=password)
            user.role = CustomUser.SCHOOL
            user.save()

            school = school_form.save(commit=False)
            school.user = user
            school.is_approved = True
            school_name = school_form.cleaned_data['school_name']
            school.slug = slugify(school_name)+'-'+str(user.id)
            school.save()

            messages.success(request, 'Account has been registered sucessfully!')
            return redirect('admin-view-AllSchools')
        else:
            messages.error(request, 'Something went wrong')
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        school_form = SchoolForm()

    context = {
        'form': form,
        'school_form': school_form,
    }

    return render(request, 'school/admin_addSchool.html', context)


# ========== Super-Admin approve Schools ========== #
@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_Approve_AllSchools(request):
    allSchools = School.objects.filter(is_approved=False)
    if request.method == 'POST':
        school_id = request.POST.getlist('approve')
        for i in school_id:
            School.objects.filter(pk=int(i)).update(is_approved=True)
        messages.success(request, 'School(s) Account has been Approved sucessfully!')
        return redirect('admin-view-AllSchools')

    context = {
        'allSchools': allSchools,
    }
    return render(request,'school/admin_Approve_Schools.html', context=context)



# ========== Super-Admin View all Schools ========== #
@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_view_AllSchools(request):
    allSchools = School.objects.annotate(no_of_department=Count('department'), no_of_students=Count('student'))
    context = {
        'allSchools': allSchools,
    }
    return render(request,'school/admin_view_allSchool.html',context=context)



# ========== Super-Admin View School Detail ========== #
@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_viewschool_detail(request, school_slug):
    school = get_object_or_404(School, slug=school_slug)
    school_departments = Department.objects.filter(school=school).annotate(no_of_students=Count('student_department'))

    departments_count = Department.objects.filter(school=school).count()
    students = Student.objects.filter(school=school)
    students_count = Student.objects.filter(school=school).count()
    context = {
        'school': school,
        'school_departments': school_departments,
        'students_count': students_count,
        'students': students,
        'departments_count': departments_count,
    }

    return render(request, 'school/admin_viewschool_detail.html', context)


# ========== Super-Admin Delete School ========== #
@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_School_Delete(request, school_slug):
    school = get_object_or_404(School, slug=school_slug)
    user = CustomUser.objects.get(email = school.user)
    school.delete()
    user.delete()
    messages.success(request, 'School Deleted')
    return redirect('admin-view-AllSchools')


@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_view_department(request, pk=None):
    school = get_object_or_404(School, pk=pk)
    departments = Department.objects.filter(school=school)
    # students = Student.objects.filter(department=departments).count()
    context = {
        'school': school,
        'departments': departments,
        # 'students': students,
    }
    return render(request, 'school/adminview_school_department.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_students_by_school(request, pk=None):
    school = get_object_or_404(School, pk=pk)
    students = Student.objects.filter(school=school)
    context = {
        'school': school,
        'students': students,
    }
    return render(request, 'school/adminview_students_by_school.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_students_by_department(request, pk=None):
    school = get_object_or_404(School, pk=pk)
    department = get_object_or_404(Department, pk=pk)
    students = Student.objects.filter(school=school, department=department)
    context = {
        'students': students,
        'department': department,
    }
    return render(request, 'school/adminview_students_by_department.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_view_students(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'school/adminview_allStudents.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def admin_view_studentsdue4payment(request):
    students = Student.objects.filter(payment_status=False)
    for students in students:
        email_address = students.email
        if request.method == 'POST':
            student_id = request.POST.getlist('payment')
            for i in student_id:       
                message = 'Congratulations you have been paid'
            
                subject = 'Payment Confirmation'
                context = {'student_name': students.fname,'message': message}
                message = get_template('school/send_email.html').render(context)
                email = EmailMessage(subject, message,"SMS Code School", [str(i)])
                email.content_subtype = "html" 
                email.send()
                return redirect('admin-view-allStudents')

    students = Student.objects.filter(payment_status=False)
    context = {
        'students': students,
    }
    return render(request, 'school/adminview_studentdue4payment.html', context)

def send_paymentconfirmationtostudent(request):
    students = Student.objects.filter(payment_status=False)
    for student in students:
        full_name = student.fname + ' ' + student.lname
        email_address = student.email
        student_id = student.id
    
        message = 'Congratulations you have been paid'
    
        subject = 'Payment confirmation'
        context = {'full_name': full_name,'message': message}
        message = get_template('school/send_email.html').render(context)
        email = EmailMessage(subject, message,"Payment confirmatation", [email_address])
        email.content_subtype = "html" 
        email.send()

        Student.objects.filter(pk=int(student_id)).update(payment_status=True)
    
    return redirect('admin-view-allStudents')




# ================== School functions ================ #

@login_required(login_url='login')
@user_passes_test(check_role_school)
def schoolDashboard(request):
    departments_count = Department.objects.filter(school = get_school(request)).count()
    students_count = Student.objects.filter(school=get_school(request)).count()

    context = {
        'departments_count': departments_count,
        'students_count': students_count,
    }
    return render(request, 'school/schoolAdmin_templates/schoolDashboard.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_school)
def school_addDept(request):
    if request.method == 'POST':
        # store the data and create the user
        form = UserForm(request.POST)
        department_form = DeptForm(request.POST)       
        if form.is_valid() and department_form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(name = name,
                                            username=username, 
                                            email=email,
                                            password=password)
            user.is_HOD = True
            user.save()

            department = department_form.save(commit=False)
            department.user = user
            department.school = get_school(request)
            department_name = department_form.cleaned_data['department_name']
            department.slug = slugify(department_name)+'-'+str(user.id)
            department.save()

            messages.success(request, 'Department has been created sucessfully!')
            return redirect('view_allDept')
        else:
            messages.error(request, 'Something went wrong')
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        department_form = DeptForm()

    context = {
        'form': form,
        'department_form': department_form,
    }

    return render(request, 'school/schoolAdmin_templates/school_addDept.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_school)
def schoolview_allDept(request):
    departments = Department.objects.filter(school = get_school(request))
    context = {
        'departments': departments,
    }
    return render(request, 'school/schoolAdmin_templates/schoolview_allDept.html', context)



# ========== SSCHOOL VIEW DEPARTMENT Detail ========== #
@login_required(login_url='login')
@user_passes_test(check_role_school)
def school_viewsdepartment_detail(request, dept_slug):
    department = get_object_or_404(Department, slug=dept_slug)
    department_students = Student.objects.filter(department=department)

    context = {
        'department': department,
        'department_students': department_students,
    }

    return render(request, 'school/schoolAdmin_templates/school_viewdepartment_detail.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_school)
def SchoolDelete_department(request, dept_slug):
    department = get_object_or_404(Department, slug=dept_slug)
    user = CustomUser.objects.get(email = department.user)
    department.delete()
    user.delete()
    messages.success(request, 'Department has been Deleted successfully')
    return redirect('view_allDept')


@login_required(login_url='login')
@user_passes_test(check_role_school)
def schoolview_allStudent(request):
    students = Department.objects.filter(school = get_school(request))
    context = {
        'students': students,
    }
    return render(request, 'school/schoolAdmin_templates/schoolview_allStudents.html', context)










