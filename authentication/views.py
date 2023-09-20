from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.template.defaultfilters import slugify


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


from .models import CustomUser
from .forms import UserForm, UserInfoForm

from school.models import School, Student
from school.forms import SchoolForm

# Create your views here.

#function to detect current logged in user
def detectuser(user):
    if user.role == 1:
        redirectUrl = 'schoolDashboard'
        return redirectUrl
    elif user.role == None and user.is_HOD:
        redirectUrl = 'deptDashboard'
        return redirectUrl
    elif user.role == None and user.is_superuser:
        redirectUrl = 'adminDashboard'
        return redirectUrl


# Restrict the school from accessing the Dept page
def check_role_school(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the Dept from accessing the School page
def check_role_dept(user):
    if user.role  == None and user.is_HOD:
        return True
    else:
        raise PermissionDenied


# Restrict the Dept from accessing the School page
def check_role_superuser(user):
    if user.role  == None and user.is_superuser:
        return True
    else:
        raise PermissionDenied



def Schoolregistration(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        # store the data and create the user
        form = UserForm(request.POST)
        school_form = SchoolForm(request.POST)
        if form.is_valid() and school_form.is_valid:
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
            school_name = school_form.cleaned_data['school_name']
            school.slug = slugify(school_name)+'-'+str(user.id)
            school.save()


            messages.success(request, 'Your account has been registered sucessfully! Please wait for the approval.')
            return redirect('/')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        school_form = SchoolForm()

    context = {
        'form': form,
        'school_form': school_form,
    }

    return render(request, 'authentication/registerSchool.html', context)




def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'authentication/login.html')



@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectuser(user)
    return redirect(redirectUrl)



def logout(request):
    if request.user != None:
        auth.logout(request)
        messages.error(request, 'You have been logged out')
    return redirect("/")


@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def adminDashboard(request):
    schoolcount = School.objects.all().count()
    allstudent = Student.objects.all().count()
    pendingschoolcount = School.objects.filter(is_approved=False).count()

    context = {
        'schoolcount':schoolcount,
        'allstudent': allstudent,
        'pendingschoolcount':pendingschoolcount,
    }
    return render(request, 'authentication/adminDashboard.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_superuser)
def adminProfile(request):
    profile = request.user

    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'School info updated successfully.')
            return redirect('adminProfile')
        else:
            print(form.errors)
            messages.error(request, 'Something Went Wrong.')
    else:
        form = UserInfoForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'authentication/adminProfile.html', context)



from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'authentication/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('myAccount')