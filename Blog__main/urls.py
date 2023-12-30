from django.urls import path, include, re_path

from Blog__main import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/<slug:slug>/', views.post_detail, name="post_detail"),
]
