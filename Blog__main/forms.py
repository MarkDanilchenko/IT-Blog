from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserRegistrationFrom(UserCreationForm):
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
