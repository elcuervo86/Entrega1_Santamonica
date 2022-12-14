# Generated by Django 4.0.6 on 2022-08-24 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDisqueria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banda', models.CharField(max_length=30)),
                ('nombreDisco', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('indNacional', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vinilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banda', models.CharField(max_length=30)),
                ('nombreDisco', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('indNacional', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.DeleteModel(
            name='CDs',
        ),
        migrations.DeleteModel(
            name='Vinilos',
        ),
    ]
