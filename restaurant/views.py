from django.shortcuts import render, redirect
from restaurant.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cadapio


# Create your views here.


@login_required
def index(request):
    cardapios = Cadapio.objects.all()
    context = {'cardapios': cardapios}
    return render(request, 'restaurant/index.html', context=context)
