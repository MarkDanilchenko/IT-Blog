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
    ordering = ("-username",)


admin.site.register(models.User, User_Admin)


# The `Post_CommentInline` class is used to define an inline form for the `Post_Comment` model in the
# Django admin interface.
class Post_CommentInline(admin.TabularInline):
    model = models.Post_Comment
    extra = 1


class Post_Admin(admin.ModelAdmin):
    fieldsets = (
        (
            "Post headers and info",
            {
                "fields": ("h1", "title", "tag", "url"),
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
        (
            "Post settings",
            {
                "fields": ("author",),
            },
        ),
    )
    list_display = ("h1", "title", "url", "created_at", "author")
    search_fields = ("title", "tag", "author")
    list_filter = ("created_at", "author")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    prepopulated_fields = {"url": ("title",)}
    inlines = [Post_CommentInline]


admin.site.register(models.Post, Post_Admin)


class Post_Comment_Admin(admin.ModelAdmin):
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


admin.site.register(models.Post_Comment, Post_Comment_Admin)
