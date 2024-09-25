from django.shortcuts import render
from django.http import HttpResponse


def mensaje(request):
    return render(request, 'mensaje/index.html')


def agregar(request):
    return HttpResponse("Agrega")
# Create your views here.
