# Generated by Django 3.2.4 on 2021-06-12 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20210612_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='quantidade_bebida_1lt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade_bebida_250',
            field=models.IntegerField(verbose_name='quantidade bebida 250ml'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade_refeicao',
            field=models.IntegerField(),
        ),
    ]