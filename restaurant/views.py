from django.shortcuts import render, redirect
from restaurant.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def index(request):
    return render(request, 'restaurant/index.html')
