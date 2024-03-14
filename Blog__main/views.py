import datetime
from rest_framework import viewsets, permissions, pagination, status
from . import models, serializers
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from fuzzywuzzy import fuzz, process
from rest_framework.response import Response
from rest_framework.views import APIView
from taggit.models import Tag

# --------------------REST API----------------------
# --------------------REST API----------------------
# --------------------REST API----------------------


# pagination class by 3 items per page
class PostPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 2


# Sign up viewSet
class SignUpViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        result = self.serializer_class(data=request.data)
        result.is_valid(raise_exception=True)
        result.save()
        return Response(
            {
                "created": f'User "{result.data.get("username")}" was successfully created.'
            },
            status=status.HTTP_201_CREATED,
        )


# Browse User's profile viewSet
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        currentUser = dict(self.serializer_class(request.user, many=False).data)
        del currentUser["password"]
        return Response({"profile": currentUser}, status=status.HTTP_200_OK)


# Post viewSet
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination
    lookup_field = "url"

    def list(self, request, *args, **kwargs):
        if request.query_params.get("tag"):
            get_object_or_404(Tag, slug=request.query_params.get("tag"))
            result = models.Post.objects.filter(
                tag__slug=request.query_params.get("tag")
            ).order_by("title")
        else:
            result = models.Post.objects.all().order_by("title")
        paginator = self.pagination_class()
        paginated_result = paginator.paginate_queryset(result, request)
        serialized_result = self.serializer_class(paginated_result, many=True).data
        return paginator.get_paginated_response(serialized_result)

    def retrieve(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post, url__icontains=kwargs["post_url"].lower())
        result = self.serializer_class(post, many=False).data
        return Response(result, status=status.HTTP_200_OK)


# Tag viewSet
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def list(self, request, *args, **kwargs):
        result = Tag.objects.all()
        result = self.serializer_class(result, many=True).data
        return Response(result, status=status.HTTP_200_OK)


# Right sidebar viewSet (Related 3 posts)
class AsidePostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        if self.request.GET.get("exclude"):
            exclude = self.request.GET.get("exclude")
            get_object_or_404(models.Post, url=exclude.lower())
            result = self.serializer_class(
                models.Post.objects.exclude(url=exclude).order_by("title")[:3],
                many=True,
            ).data
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Feedback viewSet
class FeedbackView(APIView):
    serializer_class = serializers.FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        result = self.serializer_class(data=request.data)
        if result.is_valid():
            name = result.data.get("name")
            email = result.data.get("email")
            theme = result.data.get("theme")
            message = result.data.get("message")
            print(
                f"From: {name}, {email}\nTheme: {theme};\nMessage: {message};\nTo: {settings.EMAIL_HOST_USER};",
            )
            return Response(
                {"success": "Feedback was successfully sent!"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Something went wrong! Please, try again!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

            # send_mail(
            #     f"Feedback from {name} | theme: {theme}",
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     email,
            # )


# search post viewSet (fuzzywuzzy)
class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination

    def list(self, request, *args, **kwargs):
        if self.request.GET.get("search"):
            search = self.request.GET.get("search").lower()
            result = models.Post.objects.all().order_by("title")
            for i in result:
                if (
                    # `(fuzz.partial_ratio(search, str(i.title)) > 70)` is using the `fuzz` module
                    # from the `fuzzywuzzy` library to calculate the partial ratio between the
                    # `search` string and the `title` attribute of a post (`i.title`).
                    (fuzz.partial_ratio(search, str(i.title)) > 70)
                    or (fuzz.partial_ratio(search, str(i.h1)) > 70)
                    or (fuzz.partial_ratio(search, str(i.description)) > 70)
                    or (fuzz.partial_ratio(search, str(i.content)) > 70)
                    # search coincidences in tags of the post
                    or any(
                        True
                        for j in i.tag.all()
                        if fuzz.partial_ratio(search, str(j.slug)) > 70
                    )
                ):
                    continue
                else:
                    result = result.exclude(pk=i.pk)
            else:
                if len(result) == 0:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                else:
                    paginator = self.pagination_class()
                    paginated_result = paginator.paginate_queryset(result, request)
                    serialized_result = self.serializer_class(
                        paginated_result, many=True
                    ).data
                    return paginator.get_paginated_response(serialized_result)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# comments viewSet
class Post_CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Post_CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        post = get_object_or_404(
            models.Post, url__icontains=self.request.GET.get("post")
        )
        post_comments = models.Post_Comments.objects.filter(post=post).order_by(
            "-created_at"
        )
        result = self.serializer_class(post_comments, many=True).data
        return Response(result, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        post = get_object_or_404(models.Post, title=request.data.get("post"))
        result = self.serializer_class(data=request.data)
        result.is_valid(raise_exception=True)
        result.save(post=post, user=user, text=request.data.get("text"))
        return Response(
            {
                "message": "Comment is successfully created!",
                "comment_details": result.data,
            },
            status=status.HTTP_201_CREATED,
        )
