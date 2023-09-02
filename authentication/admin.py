from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *

# Register your models here.

class UserModel(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role" )

    fieldsets = (
        (None,{
            'fields': ('username', 'email', 'role')
        }),
    )


admin.site.register(CustomUser, UserModel)

