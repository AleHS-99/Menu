# Generated by Django 4.1.5 on 2023-01-30 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modalidad',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('modal', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Modalidad',
                'verbose_name_plural': 'Modalidades',
            },
        ),
        migrations.CreateModel(
            name='oferta',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.ImageField(null=True, upload_to='items')),
                ('ingredientes', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuApp.modalidad')),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'Ingredientes',
            },
        ),
    ]
