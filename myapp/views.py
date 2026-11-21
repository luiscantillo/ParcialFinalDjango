from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ProgramaForm
from .models import Programa


def crear_programa(request):
    if request.method == "POST":
        form = ProgramaForm(request.POST)
        if form.is_valid():
            programa = form.save()
            messages.success(request, f"Programa «{programa.nombre}» registrado correctamente.")
            return redirect("crear_programa")
    else:
        form = ProgramaForm()

    programas = Programa.objects.all()
    return render(request, "myapp/programa_form.html", {"form": form, "programas": programas})
