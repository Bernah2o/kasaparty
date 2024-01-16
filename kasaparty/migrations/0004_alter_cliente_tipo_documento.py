# Generated by Django 5.0.1 on 2024-01-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasaparty', '0003_alter_proveedor_tipo_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_documento',
            field=models.CharField(choices=[('CEDULA', 'Cedula'), ('NIT', 'NIT')], default='Cedula', max_length=10),
        ),
    ]
