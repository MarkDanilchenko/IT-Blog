from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=150,
        label="Username",
        help_text="Required. 150 characters or fewer.",
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        help_text="Required. Add a valid email address.",
    )

    phone = forms.CharField(
        required=False,
        max_length=15,
        label="Phone number",
        help_text="Phone number must contain only 11 digits<br> in format _(___)___-__-__.",
    )

    class Meta:
        model = models.User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "phone",
        )


class FeedbackForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your name...",
                "required": "required",
                "id": "name",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        max_length=100,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email...",
                "required": "required",
                "id": "email",
            }
        ),
    )
    theme = forms.CharField(
        required=True,
        max_length=150,
        label="Theme",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter a theme...",
                "required": "required",
                "id": "theme",
            }
        ),
    )

    message = forms.CharField(
        required=True,
        max_length=1000,
        label="Message",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter a message...",
                "required": "required",
                "id": "message",
                "rows": "5",
                "cols": "30",
            }
        ),
    )


class Post_CommentForm(forms.ModelForm):
    text = forms.CharField(
        required=True,
        max_length=1000,
        label="",
        help_text="Up to 1000 symbols",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your comment ...",
                "required": "required",
                "id": "comment",
                "rows": 5,
                "cols": 50,
            }
        ),
    )

    class Meta:
        model = models.Post_Comment
        fields = ("text",)
