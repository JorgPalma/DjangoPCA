# Generated by Django 4.2.2 on 2023-10-26 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_persona_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido_mate',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido_pat',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='digito_ver',
            field=models.CharField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='persona',
            name='imagen',
            field=models.ImageField(default='default.png', null=True, upload_to='perfil'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='primer_nombre',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.IntegerField(default=12345678),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundo_nombre',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(default=123456789),
        ),
    ]