# Generated by Django 5.0 on 2024-01-04 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog__main', '0007_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='text',
            field=models.TextField(help_text='Comment text (max: 1000 symbols)', max_length=1000, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='user',
            field=models.ForeignKey(help_text="User's comment", on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
