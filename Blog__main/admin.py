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

    list_filter = ("is_staff", "is_active", "is_superuser", "date_joined", "last_login")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("-username",)


admin.site.register(models.User, User_Admin)


# The `Post_CommentInline` class is used to define an inline form for the `Post_Comments` model in the
# Django admin interface.
class Post_CommentsInline(admin.TabularInline):
    model = models.Post_Comments
    extra = 1


class Post_Admin(admin.ModelAdmin):
    fieldsets = (
        (
            "Post headers and other info",
            {
                "fields": ("h1", "title", "tag", "url", "author"),
            },
        ),
        (
            "Post content",
            {
                "fields": ("description", "content"),
            },
        ),
        (
            "Post image",
            {
                "fields": ("image",),
            },
        ),
    )
    list_display = ("h1", "title", "url", "created_at", "author")
    search_fields = ("h1", "title", "tag", "author")
    list_filter = ("created_at", "author")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    prepopulated_fields = {"url": ("title",)}
    inlines = [Post_CommentsInline]


admin.site.register(models.Post, Post_Admin)


class Post_Comments_Admin(admin.ModelAdmin):
    fieldsets = (
        (
            "Related Info",
            {
                "fields": ("post", "user"),
            },
        ),
        (
            "Comment",
            {
                "fields": ("text",),
            },
        ),
    )
    list_display = ("post", "user", "text", "created_at")
    search_fields = ("post", "user")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


admin.site.register(models.Post_Comments, Post_Comments_Admin)
