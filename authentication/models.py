from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    SCHOOL = 1
    ROLE = ((SCHOOL, "School"),)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=11, choices=ROLE)
    is_HOD = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.first_name
    
    def get_role(self):
        if self.role == 1:
            user_role = 'School'
        return user_role
    



