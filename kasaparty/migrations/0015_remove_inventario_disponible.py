# Generated by Django 5.0.1 on 2024-01-16 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kasaparty', '0014_alter_evento_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='disponible',
        ),
    ]
