# Generated by Django 4.2 on 2023-10-07 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size_variant',
        ),
    ]
