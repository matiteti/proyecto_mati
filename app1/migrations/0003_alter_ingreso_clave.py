# Generated by Django 4.2.3 on 2023-08-12 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso',
            name='clave',
            field=models.IntegerField(),
        ),
    ]
