# Generated by Django 5.0.1 on 2024-01-17 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasaparty', '0004_reserva_cotizacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='productos',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='evento',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='kasaparty.evento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='inventarios_propios',
            field=models.ManyToManyField(blank=True, related_name='cotizaciones_propias+', to='kasaparty.inventariopropio'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='inventarios_proveedores',
            field=models.ManyToManyField(blank=True, related_name='cotizaciones_proveedores+', to='kasaparty.inventarioproveedor'),
        ),
    ]
