from django.db import models
from django.conf import settings
from authentication.models import CustomUser

# Create your models here.

class SchoolSession(models.Model):
    session_label = models.CharField(max_length=50)

class SchoolSms(models.Model):
    user = models.ManyToManyField(CustomUser, related_name='user')
    school_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=15)
    email = models.CharField(unique=True, max_length=20)


class Department(models.Model):
    user = models.OneToOneField(CustomUser, related_name='dept_user', on_delete = models.CASCADE, blank=True, null=True)
    dept_name = models.CharField(max_length=200)
    school = models.ForeignKey(SchoolSms, on_delete=models.CASCADE, blank=True)
    dept_code = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=20)

class Student(models.Model):
    matric_no = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    school = models.ForeignKey(SchoolSms, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    acct_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

