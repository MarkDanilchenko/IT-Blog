from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from Blog__main import views


router = DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "accounts/signup/", views.SignUpView.as_view({"post": "create"}), name="signup"
    ),
    path("accounts/profile/", views.ProfileView.as_view({"get": "list"}), name="profile"),
    path("tags/", views.TagViewSet.as_view({"get": "list"}), name="tags"),
    path(
        "tags/<slug:slug>/",
        views.PostByTagViewSet.as_view({"get": "list"}),
        name="posts_by_tag",
    ),
    path(
        "aside/", views.AsidePostsViewSet.as_view({"get": "list"}), name="aside_posts"
    ),
    path("feedback/", views.FeedbackView.as_view(), name="feedback"),
    # fuzzywuzzy search
    path("search/", views.SearchView.as_view(), name="search"),
    # simple drf search is used via posts/?q=...
    # path('', views.index, name="index"),
    # path('blog/<slug:slug>/', views.post_detail, name="post_detail"),
    # path('blog/comment/<slug:slug>/', views.post_comment, name="post_comment"),
    # path('feedback/', views.feedback, name="feedback"),
    # path('feedback/success/', views.success, name="success"),
    # path('search/', views.search, name="search"),
    # path('tag/<slug:slug>/', views.tag_detail, name="tag_detail"),
]
