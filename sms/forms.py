from django import forms
from django.contrib.auth.models import User
from . import models


#for School related form
class SchoolUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','password']


class SchoolSmsForm(forms.ModelForm):
    class Meta:
        model=models.SchoolSms
        fields=['username', 'school_name', 'address', 'mobile', 'roll','status']



#for Department related form
class DepartmentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model=models.Department
        fields=['dept_name', 'dept_code', 'school','email']

