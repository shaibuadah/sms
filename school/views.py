from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.template.defaultfilters import slugify

from authentication.forms import UserForm, UserInfoForm
from authentication.models import CustomUser
from authentication.views import check_role_superuser, check_role_school, check_role_dept

from .models import School, Department, Student
from .forms import SchoolForm, SchoolInfoForm


# Get Current Logedin School
def get_school(request):
    school = School.objects.get(user=request.user)
    return school


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

