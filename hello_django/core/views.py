from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('Hello world !')


def soma(request, n1, n2):
    return HttpResponse(f'A soma de {n1} + {n2} é {n1+n2}')