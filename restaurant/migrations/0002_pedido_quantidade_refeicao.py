# Generated by Django 3.2.4 on 2021-06-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='quantidade_refeicao',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
