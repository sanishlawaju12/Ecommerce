# Generated by Django 4.2 on 2023-05-18 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_size_sizevariant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='subtotal',
        ),
    ]
