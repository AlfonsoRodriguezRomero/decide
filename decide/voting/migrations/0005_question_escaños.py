# Generated by Django 2.0 on 2020-01-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_questionoption_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='escaños',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
