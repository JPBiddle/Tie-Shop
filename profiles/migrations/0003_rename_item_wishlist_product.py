# Generated by Django 3.2.25 on 2024-06-20 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='item',
            new_name='product',
        ),
    ]
