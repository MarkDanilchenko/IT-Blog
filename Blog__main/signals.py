"""
    The code defines signal receivers in Django to perform actions when a user is created or deleted,
    such as sending email notifications or printing messages.
    
    :param sender: The `sender` parameter in the Django signal receivers refers to the model class that
    sends the signal. In this case, for the `user_joined` and `user_deleted` functions, the sender is
    the `User` model from the `models` module in your Django application.
    :param instance: The `instance` parameter in the provided Django signal handlers refers to the
    instance of the `User` model that triggered the signal (either after creation or deletion).
    :param created: The `created` parameter in the `user_joined` function is a boolean value that
    indicates whether the `User` instance was created or not. It will be `True` if the instance was
    created and `False` if it was not.
    :param kwargs: The `kwargs` parameter in the `user_joined` function is a dictionary of
    additional keyword arguments that can be passed to the signal handler. In this case, it is
    empty.
    """

from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from . import models


@receiver([post_save], sender=models.User)
def user_joined(sender, instance, created, **kwargs):
    if created:
        # send_mail(
        #     f"Welcome, {instance.username}!",
        #     f"{instance.username}, You have successfully joined our site!",
        #     f"{settings.EMAIL_HOST_USER}",
        #     [instance.email],
        # )
        print(f"{instance.username} joined!")


@receiver([post_delete], sender=models.User)
def user_deleted(sender, instance, **kwargs):
    # send_mail(
    #     f"Goodbye, {instance.username}!",
    #     f"{instance.username}, You have successfully deleted our from our site!",
    #     f"{settings.EMAIL_HOST_USER}",
    #     [instance.email],
    # )
    print(f"{instance.username} deleted!")
