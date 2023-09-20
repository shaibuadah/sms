from django import forms
from .models import School, Department, Student
from authentication.models import CustomUser

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name',]


class SchoolInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'address', 'about', 'mobile', 'state',]

class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name']

class DeptInfoForm(forms.ModelForm):
    model = CustomUser
    fields = ['username', 'email', 'mobile']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matric_no', 'fname', 'lname', 'bank_name', 'account_number', 'mobile', 'email', 'payment_status']
