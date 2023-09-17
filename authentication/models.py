from django.db import models
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    SCHOOL = 1
    ROLE = (
        (SCHOOL, 'School'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True, max_length=255)
    state = models.CharField(max_length=15, blank=True, null=True)
    about = models.TextField(blank=True, null=True, max_length=255)
    role = models.PositiveSmallIntegerField(choices=ROLE, blank=True, null=True)
    is_HOD = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    
    def get_role(self):
        if self.role == 1:
            user_role = 'School'
        return user_role


