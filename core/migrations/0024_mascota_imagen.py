# Generated by Django 4.2.2 on 2023-11-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_delete_imagenblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
