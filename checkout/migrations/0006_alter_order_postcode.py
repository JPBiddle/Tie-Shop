# Generated by Django 3.2.25 on 2024-06-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_order_town_or_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
