# Generated by Django 4.0.5 on 2022-06-16 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_alter_compra_raza_alter_compra_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.producto'),
        ),
    ]