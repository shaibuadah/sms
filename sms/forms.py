from django import forms
from django.contrib.auth.models import User
from . import models



class SchoolSmsForm(forms.ModelForm):
    class Meta:
        model=models.SchoolSms
        fields=['school_name', 'address', 'mobile', 'email']



        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model=models.Department
        fields=['dept_name', 'dept_code' ,'email']