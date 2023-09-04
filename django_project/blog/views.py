from django.http import HttpResponse
from django.shortcuts import render

post = [
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2023 UTC",
    },
    {
        "author": "Babak Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2023 UTC",
    },
]


def home(request):
    context = {"posts": post}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
