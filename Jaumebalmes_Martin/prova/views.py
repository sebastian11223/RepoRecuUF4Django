from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, context

# Create your views here.
# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

def index(request):
    professor = {"name":"Martín", "surname":"Casco", "age":"20"}
    template = loader.get_template('index.html')
    dades = template.render({'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})
    return HttpResponse(dades)

def index(request):
    context = {'students':ListaAlumnos,'teachers':ListaProfes}
    return render(request, 'index.html', context)





ListaProfes = [
    {
        "id": 1,
        "name":"martin",
        "surname":"casco",
        "age": 44,
        "asignatura":"matemáticas",
    },
    {
        "id": 2,
        "name": "Manuel",
        "surname": "gorge",
        "age": 200,
        "asignatura":"historia",
    },
    {
        "id": 3,
        "name": "Joan",
        "surname": "Carles",
        "age": 3,
        "asignatura":"castellano",
    }]
# Lista Alumnos
ListaAlumnos = [
    {
        "id": 1,
        "name": "Eduardo",
        "surname": "Manos",
        "age": 99,
        "clase":"2",
    },
    {
        "id": 2,
        "name": "Paco",
        "surname": "Mendez",
        "age": 3,
        "clase":"10",
    },
    {
        "id": 3,
        "name": "Fernando",
        "surname": "Comida",
        "age": 1,
        "clase":"35",
    },
    {
        "id": 4,
        "name": "Miguel Angel",
        "surname": "Angel",
        "age": 30,
        "clase":"11",
    },
    {
        "id": 5,
        "name": "Michael",
        "surname": "John",
        "age": 11,
        "clase":"33",
    },
    {
        "id": 6,
        "name": "luisa",
        "surname": "nada",
        "age": 43,
        "clase":"5",
    }]