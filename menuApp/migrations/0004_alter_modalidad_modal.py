# Generated by Django 3.2.16 on 2023-02-04 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuApp', '0003_alter_oferta_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalidad',
            name='modal',
            field=models.CharField(max_length=100, verbose_name='Oferta'),
        ),
    ]
