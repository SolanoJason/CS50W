from django.urls import path
from . import views
urlpatterns = [
    path("jason", views.jason, name="jason"),
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet")
]
