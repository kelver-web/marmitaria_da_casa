# Generated by Django 3.2.4 on 2021-06-12 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_pedido_quantidade_refeicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='quantidade_bebida_1lt',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade_bebida_250',
            field=models.IntegerField(max_length=20, verbose_name='quantidade bebida 250ml'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade_refeicao',
            field=models.IntegerField(max_length=20),
        ),
    ]
