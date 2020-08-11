from django.urls import path
from . import views

# # Si la url es un entero entonces ejecutara views.greet, sino entonces comprobara
# si la url dada es un str, y si no comprobara si es 
# un slug(cadena separada por guiones); sin embargo el slug nunca se dara porque
# cualquier url sera reconocida como un str, asi que para ver el comportamiento del
# slug se debera cambiar el orden
urlpatterns = [
    path("", views.greet, name="greet"),
    path("hello", views.hello, name="hello"),
    path("<int:name>", views.greet, name="greet"),
    path("<str:name>", views.greet, name="greet"),
    path("<slug:name>", views.slug, name="slug"),
]
