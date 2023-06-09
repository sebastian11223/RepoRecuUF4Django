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