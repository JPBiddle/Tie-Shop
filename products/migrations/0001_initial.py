# Generated by Django 3.2.25 on 2024-05-30 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', models.CharField(blank=True, default='', max_length=750, null=True)),
                ('image', models.ImageField(upload_to='uploads/product/')),
                ('image_2', models.ImageField(upload_to='uploads/product/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('colour', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.colour')),
            ],
        ),
    ]
