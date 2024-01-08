from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from fuzzywuzzy import fuzz, process
from rest_framework import viewsets, permissions, pagination, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from taggit.models import Tag
from . import models, forms, serializers
from django.core.paginator import Paginator


# # SIGN UP
# def signup(request):
#     if request.method == "POST":
#         form = forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password1")
#             signIn = authenticate(username=username, password=password)
#             login(request, signIn)
#             return redirect("/")
#     else:
#         form = forms.UserRegistrationForm()
#     return render(request, "registration/signup.html", {"form": form})


# # LOG OUT
# def logout_view(request):
#     logout(request)
#     next = request.GET.get("next")
#     return redirect(f"{next}")


# # display all posts at the main page
# def index(request):
#     result = models.Post.objects.all()
#     paginator = Paginator(result, per_page=3)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "index.html", {"page_obj": page_obj})


# # submit post's comments and return to the state before form's submition
# def post_comment(request, slug):
#     if request.method == "POST":
#         form = forms.Post_CommentForm(request.POST)
#         form.instance.user = request.user
#         form.instance.post = models.Post.objects.get(url=slug)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


# # display post's detailed info
# def post_detail(request, slug):
#     post = get_object_or_404(models.Post, url=slug)
#     common_tags = models.Post.tag.most_common()

#     # for most related posts for sidebar
#     last_posts = models.Post.objects.exclude(url=slug).order_by("-created_at")[:3]

#     # comment form for post
#     commentForm = forms.Post_CommentForm()
#     return render(
#         request,
#         "post_detail.html",
#         {
#             "post": post,
#             "common_tags": common_tags,
#             "last_posts": last_posts,
#             "commentForm": commentForm,
#         },
#     )


# # FEEDBACK
# def feedback(request):
#     if request.method == "POST":
#         form = forms.FeedbackForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             theme = form.cleaned_data["theme"]
#             message = form.cleaned_data["message"]
#             try:
#                 print(
#                     f"Feedback from {name} | theme: {theme}",
#                     message,
#                     settings.EMAIL_HOST_USER,
#                     email,
#                 )
#                 # send_mail(
#                 #     f"Feedback from {name} | theme: {theme}",
#                 #     message,
#                 #     settings.EMAIL_HOST_USER,
#                 #     email,
#                 # )
#             except Exception:
#                 pass
#             return HttpResponseRedirect("success")
#         return render(request, "feedback.html", {"form": form})
#     else:
#         form = forms.FeedbackForm()
#     return render(request, "feedback.html", {"form": form})


# # FEEDBACK successfully sent
# def success(request):
#     return render(request, "success.html")


# # search for posts
# def search(request):
#     try:
#         userSearch = request.GET["search"]
#         if userSearch == "":
#             raise Exception
#         else:
#             result = models.Post.objects.all()
#             for i in result:
#                 if (
#                     (fuzz.partial_ratio(userSearch, str(i.title)) > 70)
#                     or (fuzz.partial_ratio(userSearch, str(i.h1)) > 70)
#                     or (fuzz.partial_ratio(userSearch, str(i.description)) > 70)
#                     or (fuzz.partial_ratio(userSearch, str(i.content)) > 70)
#                 ):
#                     continue
#                 else:
#                     result = result.exclude(id=i.pk)
#             else:
#                 if len(result) == 0:
#                     notFound = (
#                         "Sorry, but there are no results for your search &#129764;"
#                     )
#                     return render(request, "search.html", {"notFound": notFound})
#                 else:
#                     resultCount = len(result)
#                     paginator = Paginator(result, per_page=3)
#                     page_number = request.GET.get("page")
#                     page_obj = paginator.get_page(page_number)
#                     return render(
#                         request,
#                         "search.html",
#                         {"page_obj": page_obj, "resultCount": resultCount},
#                     )
#     except Exception:
#         return redirect(request.META["HTTP_REFERER"])


# # search post by tag
# def tag_detail(request, slug):
#     tag = get_object_or_404(Tag, slug=slug)
#     common_tags = models.Post.tag.most_common()
#     posts = models.Post.objects.filter(tag=tag)
#     pagiantor = Paginator(posts, per_page=3)
#     page_number = request.GET.get("page")
#     page_obj = pagiantor.get_page(page_number)
#     return render(
#         request,
#         "tag.html",
#         {"title": f"#{tag}", "page_obj": page_obj, "common_tags": common_tags},
#     )


# --------------------REST API----------------------
# --------------------REST API----------------------
# --------------------REST API----------------------


# pagination class by 3 items for posts
class PostPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 3


# Posts and posts_detailed viewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all().order_by("-created_at")
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination
    lookup_field = "url"
    # search for posts
    search_fields = ["title", "h1", "description", "content"]
    filter_backends = [filters.SearchFilter]


# Tag viewSet
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"


# PostByTag viewSet
class PostByTagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs["slug"])
        return models.Post.objects.filter(tag=tag).order_by("-created_at")


# Related 3 Posts for the right sidebar
class AsidePostsViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all().order_by("-created_at")[:3]
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]


# Feedback view (on POST method and for auth users only)
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
                f"Feedback from {name} | theme: {theme}",
                message,
                settings.EMAIL_HOST_USER,
                email,
            )
            return Response(
                {"success": "Feedback successfully sent!"}, status=status.HTTP_200_OK
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


class SearchView(APIView):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination

    def get(self, request, *args, **kwargs):
        if request.query_params.get("q"):
            q = request.query_params.get("q")
            result = models.Post.objects.all()
            for i in result:
                if (
                    (fuzz.partial_ratio(q, str(i.title)) > 70)
                    or (fuzz.partial_ratio(q, str(i.h1)) > 70)
                    or (fuzz.partial_ratio(q, str(i.description)) > 70)
                    or (fuzz.partial_ratio(q, str(i.content)) > 70)
                ):
                    continue
                else:
                    result = result.exclude(id=i.pk)
            else:
                if len(result) == 0:
                    notFound = (
                        "Sorry, but there are no results for your search &#129764;"
                    )
                    return Response(
                        {"notFound": notFound}, status=status.HTTP_404_NOT_FOUND
                    )
                else:
                    paginator = self.pagination_class()
                    paginated_result = paginator.paginate_queryset(result, request)
                    serialized_result = self.serializer_class(
                        paginated_result, many=True
                    ).data

                    return paginator.get_paginated_response(serialized_result)
        else:
            return Response(
                {"error": "Please, enter search query"},
                status=status.HTTP_400_BAD_REQUEST,
            )
