# Generated by Django 5.0.9 on 2024-09-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto_de_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_de_perfil/'),
        ),
    ]
