from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.core.paginator import Paginator


# SIGN UP
def signup(request):
    if request.method == "POST":
        form = forms.UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            signIn = authenticate(username=username, password=password)
            login(request, signIn)
            return redirect("/")
    else:
        form = forms.UserRegistrationFrom()
    return render(request, "registration/signup.html", {"form": form})


# LOG OUT
def logout_view(request):
    logout(request)
    next = request.GET.get("next")
    return redirect(f"{next}")


# display all posts at the main page
def index(request):
    # return HttpResponse("Hello, World!")
    result = models.Post.objects.all()
    paginator = Paginator(result, per_page=2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj})


# display post's detailed info
def post_detail(request, slug):
    post = get_object_or_404(models.Post, url=slug)
    return render(request, "post_detail.html", {"post": post})
