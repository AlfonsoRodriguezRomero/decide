# Generated by Django 2.0 on 2020-01-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionoption',
            name='sexo',
            field=models.CharField(choices=[('hombre', 'HOMBRE'), ('mujer', 'MUJER')], default='hombre', max_length=6),
        ),
    ]
