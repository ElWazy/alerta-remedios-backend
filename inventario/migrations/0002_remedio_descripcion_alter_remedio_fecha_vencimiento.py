# Generated by Django 5.0.2 on 2024-02-27 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='remedio',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='remedio',
            name='fecha_vencimiento',
            field=models.DateTimeField(),
        ),
    ]