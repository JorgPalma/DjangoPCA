# Generated by Django 4.2.2 on 2023-11-21 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alergia_rename_ac_fisica_formulario_act_fisica_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='animal',
        ),
        migrations.AddField(
            model_name='raza',
            name='animal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='animal_mascota', to='core.animal'),
            preserve_default=False,
        ),
    ]
