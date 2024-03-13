from django.urls import path
from Blog__main import views
from django.views.generic import TemplateView


urlpatterns = [
    # test page
    path("test/", TemplateView.as_view(template_name="testPage.html"), name="test"),
    # sign up
    path(
        "accounts/signup/",
        views.SignUpViewSet.as_view({"post": "create"}),
        name="signup",
    ),
    # user's profile
    path(
        "accounts/profile/",
        views.ProfileViewSet.as_view({"get": "retrieve"}),
        name="profile",
    ),
    # posts, posts by tag (through query params - ?tag=)
    path("posts/", views.PostViewSet.as_view({"get": "list"}), name="posts"),
    # single post (details)
    path(
        "posts/<slug:post_url>/",
        views.PostViewSet.as_view({"get": "retrieve"}),
        name="post",
    ),
    # aside bar posts
    path(
        "posts_aside/",
        views.AsidePostViewSet.as_view({"get": "list"}),
        name="posts_aside",
    ),
    # tags
    path("tags/", views.TagViewSet.as_view({"get": "list"}), name="tags"),
    # feedback
    path("feedback/", views.FeedbackView.as_view(), name="feedback"),
    # search (fuzzywuzzy)
    path("search/", views.SearchViewSet.as_view({"get": "list"}), name="search"),
    # comments (GET)
    path(
        "comments/<slug:post_url>/",
        views.Post_CommentsViewSet.as_view({"get": "list"}),
        name="comments_get",
    ),
    # comments (POST)
    path(
        "comments/",
        views.Post_CommentsViewSet.as_view({"post": "create"}),
        name="comments_post",
    ),
]
