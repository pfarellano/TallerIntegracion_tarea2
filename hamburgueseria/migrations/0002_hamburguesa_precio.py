# Generated by Django 3.0.5 on 2020-04-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgueseria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburguesa',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
