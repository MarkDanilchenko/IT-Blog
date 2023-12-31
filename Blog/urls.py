"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Blog__main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("Blog__main.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/token_refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path('accounts/logout/', views.logout_view, name="logout"),
    # path("accounts/signup", views.signup, name="signup"),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
