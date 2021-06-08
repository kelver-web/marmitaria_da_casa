from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proteinas = models.CharField(max_length=100)
    acompanhamentos = models.CharField(max_length=100)
    saladas = models.CharField(max_length=80)
    valor_refeicao = models.DecimalField(max_digits=10, decimal_places=2)
    sabor_bebida250 = models.CharField(max_length=20, verbose_name='sabor de 250ml')
    quantidade_bebida_250 = models.CharField(max_length=20, verbose_name='quantidade bebida 250ml')
    bebida_1lt = models.CharField(max_length=15)
    quantidade_bebida_1lt = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Cadapio(models.Model):
    nome = models.CharField(max_length=40)
    proteina = models.CharField(max_length=70) 
    acompanhamento = models.CharField(max_length=150)
    salada = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = 'Cadapio'

    def __str__(self):
        return self.nome
