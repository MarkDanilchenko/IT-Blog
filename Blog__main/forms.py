from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        help_text="Required. 150 characters or fewer.<br> Letters, digits and @/./+/-/_ only.",
    )
    email = forms.EmailField(
        required=True, help_text="Required. Add a valid email address.", label="Email"
    )

    phone = forms.CharField(
        max_length=15,
        required=False,
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
        max_length=100,
        required=True,
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
        max_length=100,
        required=True,
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
        max_length=250,
        required=False,
        label="Theme",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter a theme...",
                "id": "theme",
            }
        ),
    )

    message = forms.CharField(
        max_length=1000,
        required=True,
        label="Message",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter a message...",
                "id": "message",
                "required": "required",
                "rows": "5",
            }
        ),
    )
