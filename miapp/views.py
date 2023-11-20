from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"index.html")
def cursos(request):
    cursos = ['Lenguaje de Programacion 3', 'Legislacion Informatica', 
              'Ingenieria de Requerimientos', 'Algoritmos de Computacion Grafica', 
              'Microprocesadores', 'Gestion de Procesos de Negocios', 'Dinamica de Sistemas']
    return render(request, 'cursos.html', {'cursos': cursos})

def primos(request, a=1, b=100):
    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
    
    numeros_primos = [num for num in range(a, b+1) if es_primo(num)]

    return render(request, 'primos.html', {'a': a, 'b': b, 'numeros_primos': numeros_primos})

def examen(request):
    examen = [
        {'name': 'Marcani Diaz Terry Anthony', 'github': 'https://github.com/Terry033/UC3_Parte01.git'},
        {'name': 'Muñoz Cosme Anibal Ronald', 'github': 'https://github.com/anibalronald/UC3-Parte02.git'},
        {'name': 'Mondragon Parodi Alberto Ismael', 'github': 'https://github.com/Mondra1025/UC3-Parte03-.git'},
        {'name': 'Isla Cconislla Brandon Jame', 'github': 'https://github.com/brandonjame/UC3-Parte04.git'},
    ]
    return render(request, 'examen.html', {'examen': examen})