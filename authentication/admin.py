from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *

# Register your models here.

class UserModel(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role" )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, UserModel)

