from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request, newyear= (datetime.now().day == 11 and datetime.now().month == 1)):
    return render(request, "newyear/index.html", {
        "date": newyear
    })