# Generated by Django 3.2.25 on 2024-06-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_rename_uantity_orderlineitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
