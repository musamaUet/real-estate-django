# Generated by Django 5.0.3 on 2024-03-20 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='descriuption',
            new_name='description',
        ),
    ]
