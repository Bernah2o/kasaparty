# Generated by Django 5.0.1 on 2024-01-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasaparty', '0005_remove_cotizacion_productos_cotizacion_evento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
