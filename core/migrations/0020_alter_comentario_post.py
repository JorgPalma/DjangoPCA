# Generated by Django 4.2.2 on 2023-11-10 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_comentario_post_alter_comentario_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentario_post', to='core.blog'),
        ),
    ]