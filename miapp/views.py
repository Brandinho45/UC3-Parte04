from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"index.html")
def cursos(request):
    cursos = ['Lenguaje de Programacion 3', 'Legislacion Informatica', 
              'Ingenieria de Requerimientos', 'Algoritmos de Computacion Grafica', 
              'Microprocesadores', 'Gestion de Procesos de Negocios', 'Dinamica de Sistemas']
    return render(request, 'cursos.html', {'cursos': cursos})