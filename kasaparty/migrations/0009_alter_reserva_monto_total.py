# Generated by Django 5.0.1 on 2024-01-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasaparty', '0008_alter_cotizacion_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='monto_total',
            field=models.IntegerField(blank=True),
        ),
    ]
