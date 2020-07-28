from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    bool = now.month == 1 and now.day == 1
    return render(request, "newyear/year.html", {
    "newyear": bool
    })
