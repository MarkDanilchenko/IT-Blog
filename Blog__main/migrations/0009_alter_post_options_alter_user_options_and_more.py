# Generated by Django 5.0 on 2024-03-10 16:06

import Blog__main.models
import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog__main', '0008_alter_post_comment_text_alter_post_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-username'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='Author', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Content', verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, help_text='Created at', verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Description', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='h1',
            field=models.CharField(help_text='H1', max_length=100, verbose_name='H1'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Image', null=True, upload_to='IMG', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Title', max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(help_text='URL', verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Email', max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, help_text='First name', max_length=100, validators=[Blog__main.models.name_validator], verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, help_text='Last name', max_length=100, validators=[Blog__main.models.name_validator], verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Username', max_length=100, unique=True, verbose_name='Username'),
        ),
        migrations.CreateModel(
            name='Post_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Text (max: 1000 symbols)', max_length=1000, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at', verbose_name='Created at')),
                ('post', models.ForeignKey(help_text='Commented post', on_delete=django.db.models.deletion.CASCADE, to='Blog__main.post', verbose_name='Commented post')),
                ('user', models.ForeignKey(help_text='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Post_Comment',
                'verbose_name_plural': 'Post_Comments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Post_Comment',
        ),
    ]