from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Aqui será a página principal da marmitaria da casa</h1>')