# Generated by Django 4.2.10 on 2024-03-20 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_profile_direccion_profile_email_profile_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
