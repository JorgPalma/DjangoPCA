# Generated by Django 4.2.2 on 2023-11-21 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0025_remove_mascota_raza_animal_raza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_alergia', models.CharField(default='No', max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='ac_fisica',
            new_name='act_fisica',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='enferme_ante',
            new_name='antec_enfermedades',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='vacunas',
            new_name='edad',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='raza',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='alergias',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='tiene_alergias',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='tiene_enfermedad',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='tiene_operaciones',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='tiene_sintomas',
        ),
        migrations.AddField(
            model_name='formulario',
            name='num_vacunas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='peso',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='tamanio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='raza_mascota', to='core.raza'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formulario',
            name='nombre_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_formulario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='operaciones',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='sintomas',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='formulario',
            name='alergia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='alergia', to='core.alergia'),
            preserve_default=False,
        ),
    ]
