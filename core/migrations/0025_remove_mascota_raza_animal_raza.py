# Generated by Django 4.2.2 on 2023-11-21 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_mascota_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='raza',
        ),
        migrations.AddField(
            model_name='animal',
            name='raza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='raza_mascota', to='core.raza'),
            preserve_default=False,
        ),
    ]
