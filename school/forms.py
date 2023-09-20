from django import forms
from .models import School, Department, Student
from authentication.models import CustomUser

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name','mobile', 'Address']


class SchoolInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'mobile',]

class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_code']

class DeptInfoForm(forms.ModelForm):
    model = CustomUser
    fields = ['email', 'mobile']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matric_no', 'fname', 'lname', 'bank_name', 'account_number', 'mobile', 'email', 'payment_status']
