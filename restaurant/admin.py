from django.contrib import admin
from django.db import models
from restaurant.models import Pedido

# Register your models here.


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'proteinas', 'acompanhamentos', 'saladas', 'valor_refeicao',
                    'sabor_bebida250', 'quantidade_bebida_250', 'bebida_1lt',
                    'quantidade_bebida_1lt', 'nome', 'endereco', 'numero', 'bairro', 'email', 'telefone',  'data', 'observacao'
                    ]

    list_filter = ('usuario', 'nome', 'data')
    ordering = ('usuario', )


admin.site.register(Pedido, PedidoAdmin)
