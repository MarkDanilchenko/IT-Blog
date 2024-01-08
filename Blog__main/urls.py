from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from Blog__main import views


router = DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
    # path('', views.index, name="index"),
    # path('blog/<slug:slug>/', views.post_detail, name="post_detail"),
    # path('blog/comment/<slug:slug>/', views.post_comment, name="post_comment"),
    # path('feedback/', views.feedback, name="feedback"),
    # path('feedback/success/', views.success, name="success"),
    # path('search/', views.search, name="search"),
    # path('tag/<slug:slug>/', views.tag_detail, name="tag_detail"),
]
