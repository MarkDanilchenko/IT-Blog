from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from Blog__main import views


router = DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "accounts/signup/",
        views.SignUpViewSet.as_view({"post": "create"}),
        name="signup",
    ),
    path(
        "accounts/profile/",
        views.ProfileViewSet.as_view({"get": "list"}),
        name="profile",
    ),
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
    # SEARCH ----->
    # fuzzywuzzy: via search/?q=...
    # DRF with views.PostViewSet: via posts/?q=...
    path("search/", views.SearchView.as_view(), name="search"),
    path(
        "comments/",
        views.Post_CommentViewSet.as_view({"post": "create"}),
        name="create_comment",
    ),
    path(
        "comments/<slug:post_slug>/",
        views.Post_CommentViewSet.as_view({"get": "list"}),
        name="get_post_comments",
    ),
]
