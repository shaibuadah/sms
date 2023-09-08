from django.db import models
from django.conf import settings
from authentication.models import CustomUser



# Create your models here.

class SchoolSms(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user', on_delete = models.CASCADE, blank=True, null=True)
    school_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=15)
    email = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.school_name


class Department(models.Model):
    user = models.OneToOneField(CustomUser, related_name='dept_user', on_delete = models.CASCADE, blank=True, null=True)
    dept_name = models.CharField(max_length=200)
    school = models.ForeignKey(SchoolSms, on_delete=models.CASCADE, blank=True, related_name='departments')
    dept_code = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.dept_name

class Student(models.Model):
    matric_no = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    school = models.ForeignKey(SchoolSms, on_delete=models.CASCADE, related_name='student')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_department')
    acct_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.fname