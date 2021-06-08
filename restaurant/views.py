from django.shortcuts import render, redirect
from restaurant.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cadapio, Pedido


# Create your views here.


@login_required
def index(request):
    cardapios = Cadapio.objects.all()
    context = {'cardapios': cardapios}
    return render(request, 'restaurant/index.html', context=context)


@login_required
def pedido(request):
    if request.method == 'POST':
        proteinas = request.POST.get('proteina')
        sabor_bebida250 = request.POST.get('bebidapequena')
        acompanhamentos = request.POST.get('acompanhamentos')
        quantidade_bebida_250 = request.POST.get('quantidadeBebidaPequena')
        saladas = request.POST.get('saladas')
        bebida_1lt = request.POST.get('bebidaGrande')
        valor_refeicao = request.POST.get('valorrefeicao')
        quantidade_bebida_1lt = request.POST.get('bebidadeumlt')
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        observacao = request.POST.get('observacao')
        usuario = request.user

        id = request.POST.get('id')

        if id:
            pedidos = Pedido.objects.get(id=id)

            if pedidos.usuario == usuario:
                pedido.proteinas = proteinas
                pedido.sabor_bebida250 = sabor_bebida250
                pedido.acompanhamentos = acompanhamentos
                pedido.quantidade_bebida_250 = quantidade_bebida_250
                pedido.saladas = saladas
                pedido.bebida_1lt = bebida_1lt
                pedido.valor_refeicao = valor_refeicao
                pedido.quantidade_bebida_1lt = quantidade_bebida_1lt
                pedido.nome = nome
                pedido.endereco = endereco
                pedido.numero = numero
                pedido.bairro = bairro
                pedido.telefone = telefone
                pedido.email = email
                pedido.observacao = observacao

        else:
            Pedido.objects.create(proteinas=proteinas, sabor_bebida250=sabor_bebida250,
                                acompanhamentos=acompanhamentos, quantidade_bebida_250=quantidade_bebida_250,
                                saladas=saladas, bebida_1lt=bebida_1lt, valor_refeicao=valor_refeicao,quantidade_bebida_1lt=quantidade_bebida_1lt, nome=nome, endereco=endereco, numero=numero, bairro=bairro, telefone=telefone, email=email, observacao=observacao, usuario=usuario)
    return redirect('/index')