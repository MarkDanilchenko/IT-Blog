from django.urls import path, include, re_path

from Blog__main import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
]
