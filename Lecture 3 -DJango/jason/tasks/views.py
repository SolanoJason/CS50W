from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# Creando el formulario desde aqui podemos realizar una doble validacion, 
# del lado del cliente y del lado del servidor
# Esto sirve en caso de que por alguna razon la validacion en el cliente
# no es la misma que la del servidor, esto se da cuando cambiamos la 
# validacion del servidor, sin embargo antes de que lo cambiemos 
# el cliente sigue abierto y no se ha actualizado, por lo que del lado
# del cliente se podria romper la validacion
class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task:")
    priority = forms.IntegerField(label="Priority:", max_value=1)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == 'POST':
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form                
            })
    return render(request, "tasks/add.html", {
        "form": newTaskForm()
    })
