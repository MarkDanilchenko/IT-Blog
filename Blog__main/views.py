from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from fuzzywuzzy import fuzz, process
from taggit.models import Tag
from . import models, forms
from django.core.paginator import Paginator


# SIGN UP
def signup(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            signIn = authenticate(username=username, password=password)
            login(request, signIn)
            return redirect("/")
    else:
        form = forms.UserRegistrationForm()
    return render(request, "registration/signup.html", {"form": form})


# LOG OUT
def logout_view(request):
    logout(request)
    next = request.GET.get("next")
    return redirect(f"{next}")


# display all posts at the main page
def index(request):
    result = models.Post.objects.all()
    paginator = Paginator(result, per_page=2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj})


# display post's detailed info
def post_detail(request, slug):
    post = get_object_or_404(models.Post, url=slug)
    common_tags = models.Post.tag.most_common()

    # for most related posts for sidebar
    last_posts = models.Post.objects.exclude(url=slug).order_by("-created_at")[:3]
    return render(
        request,
        "post_detail.html",
        {"post": post, "common_tags": common_tags, "last_posts": last_posts},
    )


# FEEDBACK
def feedback(request):
    if request.method == "POST":
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            theme = form.cleaned_data["theme"]
            message = form.cleaned_data["message"]
            try:
                send_mail(
                    f"Feedback from {name} | theme: {theme}",
                    message,
                    email,
                    settings.EMAIL_HOST_USER,
                )
            except Exception:
                pass
            return HttpResponseRedirect("success")
        return render(request, "feedback.html", {"form": form})
    else:
        form = forms.FeedbackForm()
    return render(request, "feedback.html", {"form": form})


# FEEDBACK successfully sent
def success(request):
    return render(request, "success.html")


# search for posts
def search(request):
    try:
        userSearch = request.GET["search"]
        if userSearch == "":
            raise Exception
        else:
            result = models.Post.objects.all()
            for i in result:
                if (
                    (fuzz.partial_ratio(userSearch, str(i.title)) > 70)
                    or (fuzz.partial_ratio(userSearch, str(i.h1)) > 70)
                    or (fuzz.partial_ratio(userSearch, str(i.description)) > 70)
                    or (fuzz.partial_ratio(userSearch, str(i.content)) > 70)
                ):
                    continue
                else:
                    result = result.exclude(id=i.pk)
            else:
                if len(result) == 0:
                    notFound = (
                        "Sorry, but there are no results for your search &#129764;"
                    )
                    return render(request, "search.html", {"notFound": notFound})
                else:
                    resultCount = len(result)
                    paginator = Paginator(result, per_page=2)
                    page_number = request.GET.get("page")
                    page_obj = paginator.get_page(page_number)
                    return render(
                        request,
                        "search.html",
                        {"page_obj": page_obj, "resultCount": resultCount},
                    )
    except Exception:
        return redirect(request.META["HTTP_REFERER"])


# search post by tag
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = models.Post.tag.most_common()
    posts = models.Post.objects.filter(tag=tag)
    pagiantor = Paginator(posts, per_page=2)
    page_number = request.GET.get("page")
    page_obj = pagiantor.get_page(page_number)
    return render(
        request,
        "tag.html",
        {"title": f"#{tag}", "page_obj": page_obj, "common_tags": common_tags},
    )
