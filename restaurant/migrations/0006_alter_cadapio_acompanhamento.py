# Generated by Django 3.2.4 on 2021-06-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_cadapio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadapio',
            name='acompanhamento',
            field=models.CharField(max_length=150),
        ),
    ]
