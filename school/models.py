from django.db import models
from authentication.models import CustomUser

# Create your models here.


class School(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    Address = models.TextField()
    mobile = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school_name
    


class Department(models.Model):
    user = models.OneToOneField(CustomUser, related_name='dept_user', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=50)
    department_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def clean(self):
        self.department_name = self.department_name.capitalize()
    
    def __str__(self):
        return self.department_name


class Student(models.Model):
    matric_no = models.CharField(max_length=15, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_department')
    bank_name = models.CharField(max_length=10)
    account_number = models.CharField(max_length=250, blank=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.matric_no +' ' + self.fname + ' ' + self.lname