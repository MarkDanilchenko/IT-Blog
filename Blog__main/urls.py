from django.urls import path, include, re_path

from Blog__main import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/<slug:slug>/', views.post_detail, name="post_detail"),
    path('feedback/', views.feedback, name="feedback"),
    path('feedback/success/', views.success, name="success"),
    path('search/', views.search, name="search"),
    path('tag/<slug:slug>/', views.tag_detail, name="tag_detail"),
]
