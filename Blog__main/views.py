from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator


# display all posts at the main page
def index(request):
    result = models.Post.objects.all()
    paginator = Paginator(result, per_page=2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj})


def post_detail(request, slug):
    post = get_object_or_404(models.Post, url=slug)
    return render(request, "post_detail.html", {"post": post})
