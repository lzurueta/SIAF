# Generated by Django 4.2.10 on 2024-03-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_profile_activate_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='disabled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]