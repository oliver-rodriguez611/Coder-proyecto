# Generated by Django 5.1.1 on 2024-09-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_productos', '0003_empleados'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='cargo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
