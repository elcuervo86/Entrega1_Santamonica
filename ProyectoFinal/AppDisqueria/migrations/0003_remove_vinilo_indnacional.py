# Generated by Django 4.0.6 on 2022-08-24 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppDisqueria', '0002_cd_vinilo_rename_clientes_cliente_delete_cds_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vinilo',
            name='indNacional',
        ),
    ]