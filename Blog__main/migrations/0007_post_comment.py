# Generated by Django 5.0 on 2024-01-03 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog__main', '0006_remove_post_tag_post_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Comment text', verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date of comment creation', verbose_name='Created at')),
                ('post', models.ForeignKey(help_text='Comment on post', on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='Blog__main.post', verbose_name='Post')),
                ('user', models.ForeignKey(help_text="User's comment", on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Post_Comment',
                'verbose_name_plural': 'Post_Comments',
                'ordering': ['-created_at'],
            },
        ),
    ]
