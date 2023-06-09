from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,loader

# def index(request):
#     professor = {"name":"Martín", "surname":"Casco", "age":"20"}
#     template = loader.get_template('index.html')
#     dades = template.render({'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})
#     return HttpResponse(dades)

def index(request):
#    template = loader.get_template('index.html')
#    return HttpResponse(template.render())
    context = {'students':ListaAlumnos,'teachers':ListaProfes}
    return render(request, 'index.html', context)


# def student(request):
#     estudiantes = {"name":"Pepe", "surname":"Perales", "age":"25", "clase":"2"}
#     contexto = {'estudiantes': estudiantes}
#     return render(request, 'students.html', contexto)

# def teachers(request):
#     profesores = {"name":"Juan", "surname":"Ronda", "age":"50", "asignatura":"matemáticas"}
#     context = {'profes': profesores}
#     return render(request,'teachers.html', context)


def student(request):
   
    contexto = {'estudiantes': ListaAlumnos}
    return render(request, 'students.html', contexto)


def teachers(request):
    
    context = {'profes': ListaProfes}
    return render(request,'teachers.html', context)






def estudiantes(request, pk):
    student_Obj = None
    for s in ListaAlumnos:
        if s['id'] == int(pk):
            student_Obj = s
    return render(request, 'student.html', {'stu':student_Obj})

def profesores(request, pk):
    profe_Obj = None
    for t in ListaProfes:
        if t['id'] == int(pk):
            profe_Obj = t
    return render(request, 'teacher.html', {'teach': profe_Obj})




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