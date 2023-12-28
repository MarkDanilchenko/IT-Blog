from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class User_Admin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
        "last_login",
    )

    search_fields = ("username",)
    list_filter = ("is_staff", "is_active", "is_superuser", "date_joined", "last_login")


admin.site.register(models.User, User_Admin)
