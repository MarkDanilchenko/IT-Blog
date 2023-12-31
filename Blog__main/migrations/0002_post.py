# Generated by Django 5.0 on 2023-12-28 20:01

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog__main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=100, verbose_name='H1')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('url', models.URLField(verbose_name='URL')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Description')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('tag', models.CharField(max_length=100, verbose_name='Tag')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
