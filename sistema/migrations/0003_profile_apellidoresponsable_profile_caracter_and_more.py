# Generated by Django 4.2.10 on 2024-03-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_profile_direccion_profile_email_profile_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apellidoResponsable',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='caracter',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='dni',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nombreResponsable',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]