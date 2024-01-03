import re
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from taggit.managers import TaggableManager


def validate_phone(value):
    if re.search(r"\d{1}\(\d{3}\)\d{3}-\d{2}-\d{2}", value) is None:
        raise ValidationError(
            "Phone number should contain only 11 digits in format _(___)___-__-__."
        )
    else:
        return f"+{value}"


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Username",
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
    )

    phone = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        validators=[validate_phone],
        verbose_name="Phone number",
        help_text="Phone number should contain only 11 digits in format _(___)___-__-__.",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}, ID: ({self.pk})"


class Post(models.Model):
    h1 = models.CharField(max_length=100, verbose_name="H1")
    title = models.CharField(max_length=200, verbose_name="Title")
    url = models.SlugField(verbose_name="URL")
    description = RichTextUploadingField(verbose_name="Description")
    content = RichTextUploadingField(verbose_name="Content")
    image = models.ImageField(
        upload_to="IMG", blank=True, verbose_name="Image", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    # tag = models.CharField(max_length=100, verbose_name="Tag")
    tag = TaggableManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
