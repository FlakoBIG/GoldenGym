# Generated by Django 3.2 on 2024-11-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoldenGymApp', '0004_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
