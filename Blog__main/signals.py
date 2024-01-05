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
