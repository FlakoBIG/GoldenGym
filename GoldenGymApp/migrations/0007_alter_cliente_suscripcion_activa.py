# Generated by Django 3.2 on 2024-11-20 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoldenGymApp', '0006_reporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='suscripcion_activa',
            field=models.BooleanField(default=True),
        ),
    ]
