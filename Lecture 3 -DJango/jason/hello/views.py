from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request, name="Default name"):
    return render(request, "hello/index.html", {
        "name":name
    })


def greet(request, name='unknown'):
    if type(name) is int:
        return HttpResponse(f"<h1>{(name)} is not a name</h1>")
    elif type(name) is str:
        return HttpResponse(f"<h1>Hello {(name.capitalize())}</h1>")


def slug(request, name):
    return HttpResponse(f"<h1>The url is a slug</h1>")
