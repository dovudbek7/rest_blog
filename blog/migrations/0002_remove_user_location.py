# Generated by Django 5.1.1 on 2024-09-19 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
    ]