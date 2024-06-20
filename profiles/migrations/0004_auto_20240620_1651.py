# Generated by Django 3.2.25 on 2024-06-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_description'),
        ('profiles', '0003_rename_item_wishlist_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]