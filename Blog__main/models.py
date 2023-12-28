import re

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def validate_phone(value):
    if re.search(r"\d{1}\(\d{3}\)\d{3}-\d{2}-\d{2}", value) is None:
        raise ValidationError(
            "Phone number must contain only 11 digits in format _(___)___-__-__"
        )
    else:
        return f"+{value}"


class User(AbstractUser):
    phone = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        validators=[validate_phone],
        verbose_name="Phone number",
        help_text="Phone number must contain only 11 digits in format _(___)___-__-__",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}, ID: ({self.pk})"


class Post(models.Model):
    h1 = models.CharField(max_length=100, verbose_name="H1")
    title = models.CharField(max_length=200, verbose_name="Title")
    url = models.URLField(verbose_name="URL")
    description = RichTextUploadingField(verbose_name="Description")
    content = RichTextUploadingField(verbose_name="Content")
    image = models.ImageField(upload_to="images", blank=True, verbose_name="Image", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    tag = models.CharField(max_length=100, verbose_name="Tag")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
