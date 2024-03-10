import re
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from taggit.managers import TaggableManager


# VALIDATORS
# VALIDATORS
# VALIDATORS
def validate_phone(value):
    if re.search(r"\d{1}\(\d{3}\)\d{3}-\d{2}-\d{2}", value) is None:
        raise ValidationError(
            "Phone number should contain only 11 digits in format _(___)___-__-__."
        )
    else:
        return f"+{value}"


def name_validator(value):
    """
    The function `name_validator` validates a given input value to ensure it contains only letters and
    is at least 2 characters long.
    """
    if re.search(r"^[a-zA-Z]{2,}$", value):
        return value
    else:
        raise ValueError(
            "First name or last name contains invalid characters. Only letters are allowed."
        )


class User(AbstractUser):
    username = models.CharField(
        max_length=100,
        unique=True,
        help_text="Username",
        verbose_name="Username",
    )

    first_name = models.CharField(
        validators=[name_validator],
        blank=True,
        max_length=100,
        help_text="First name",
        verbose_name="First name",
    )

    last_name = models.CharField(
        validators=[name_validator],
        blank=True,
        max_length=100,
        help_text="Last name",
        verbose_name="Last name",
    )

    email = models.EmailField(
        unique=True,
        help_text="Email",
        verbose_name="Email",
    )

    phone = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        validators=[validate_phone],
        help_text="Phone number should contain only 11 digits in format _(___)___-__-__.",
        verbose_name="Phone number",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-username"]

    def __str__(self):
        return self.username


class Post(models.Model):
    h1 = models.CharField(max_length=100, help_text="H1", verbose_name="H1")
    title = models.CharField(max_length=200, help_text="Title", verbose_name="Title")
    url = models.SlugField(help_text="URL", verbose_name="URL")
    description = RichTextUploadingField(
        help_text="Description", verbose_name="Description"
    )
    content = RichTextUploadingField(help_text="Content", verbose_name="Content")
    image = models.ImageField(
        upload_to="IMG", blank=True, help_text="Image", verbose_name="Image", null=True
    )
    created_at = models.DateField(
        auto_now_add=True, help_text="Created at", verbose_name="Created at"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="Author", verbose_name="Author"
    )
    tag = TaggableManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Post_Comments(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        help_text="Commented post",
        verbose_name="Commented post",
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="User", verbose_name="User"
    )

    text = models.TextField(
        max_length=1000,
        help_text="Text (max: 1000 symbols)",
        verbose_name="Text",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Created at",
        verbose_name="Created at",
    )

    class Meta:
        verbose_name = "Post_Comment"
        verbose_name_plural = "Post_Comments"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.text[:25]}..."
