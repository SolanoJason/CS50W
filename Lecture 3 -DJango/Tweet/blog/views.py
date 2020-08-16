from django.shortcuts import render

# Create your views here.

posts = [
    {
        'title': 'title1',
        'author': 'jason solano',
        'content': 'first post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'title': 'title2',
        'author': 'ennio pillaca',
        'content': 'first post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    return render(request, "blog/home.html", {
        "posts": posts
    })

def about(request):
    return render(request, "blog/about.html", {
        "title": "About"
    })