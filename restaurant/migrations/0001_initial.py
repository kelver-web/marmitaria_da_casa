# Generated by Django 3.2.4 on 2021-06-06 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proteinas', models.CharField(max_length=100)),
                ('acompanhamentos', models.CharField(max_length=100)),
                ('saldas', models.CharField(max_length=80)),
                ('valor_refeicao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sabor_bebida250', models.CharField(max_length=20, verbose_name='sabor de 250ml')),
                ('quantidade_bebida_250', models.IntegerField(max_length=20, verbose_name='quant. bebida 250ml')),
                ('bebida_1lt', models.CharField(max_length=15)),
                ('quantidade_bebida_1lt', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=80)),
                ('data', models.DateTimeField(auto_now=True)),
                ('usuraio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
