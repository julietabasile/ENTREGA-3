from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Estudiante, Profesor, Curso
from .forms import EstudianteForm, ProfesorForm, CursoForm

def ingresar_datos(request):
    if request.method == 'POST':
        estudiante_form = EstudianteForm(request.POST)
        profesor_form = ProfesorForm(request.POST)
        curso_form = CursoForm(request.POST)

        if estudiante_form.is_valid() and profesor_form.is_valid() and curso_form.is_valid():
            estudiante_form.save()
            profesor_form.save()
            curso_form.save()
            return redirect('ingresar_datos')

    else:
        estudiante_form = EstudianteForm()
        profesor_form = ProfesorForm()
        curso_form = CursoForm()

    return render(request, 'miapp/ingresar_datos.html', {
        'estudiante_form': estudiante_form,
        'profesor_form': profesor_form,
        'curso_form': curso_form,
    })

def buscar_cursos(request):
    # Lógica para buscar cursos en la base de datos
    pass

