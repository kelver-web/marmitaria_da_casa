from django.contrib import admin
from django.db import models
from restaurant.models import Pedido, Cadapio

# Register your models here.


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'proteinas', 'acompanhamentos', 'saladas', 'valor_refeicao',    'quantidade_refeicao',
                    'sabor_bebida250', 'quantidade_bebida_250', 'bebida_1lt',
                    'quantidade_bebida_1lt', 'endereco', 'numero', 'bairro', 'email', 'telefone',  'data', 'observacao'
                    ]

    list_filter = ('usuario', 'nome', 'data')
    ordering = ('usuario', )


class CardapioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'proteina', 'acompanhamento', 'salada']


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Cadapio, CardapioAdmin)
