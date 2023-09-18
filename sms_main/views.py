from django.shortcuts import render, redirect
from django.contrib import messages



def home(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    return render(request, 'home.html')