from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied


# Create your views here.

#function to detect current logged in user
def detectuser(user):
    if user.role == 1:
        redirectUrl = 'school-dashboard'
        return redirectUrl
    elif user.role == None and user.is_HOD:
        redirectUrl = 'department-dashboard'
        return redirectUrl
    elif user.role == None and user.is_superuser:
        redirectUrl = '/admin'
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


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            pass
        return render(request, 'authentication/login.html')

    def post(self, request):
        user = authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            return redirect('myaccount')
    
        else:
            messages.error(request, 'Invalid credentials,try again')
            return redirect("login")



@login_required(login_url='login')
def myaccount(request):
    user = request.user
    redirectUrl = detectuser(user)
    return redirect(redirectUrl)




def logout_user(request):
    if request.user != None:
        logout(request)
        messages.error(request, 'You have been logged out')
    return redirect("homepage")