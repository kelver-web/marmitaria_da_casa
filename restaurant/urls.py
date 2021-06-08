from django import urls
from django.urls import path
from django.views.generic import RedirectView
from .import views

urlpatterns = [
    path('index/', views.index),
    path('index/submit', views.pedido),
    path('', RedirectView.as_view(url='/index/')),
]