from django.db import models
from authentication.models import CustomUser

# Create your models here.


class School(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school_name
    


class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
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
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_department')
    student_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    account_number = models.TextField(max_length=250, blank=True)
    is_due4payment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name