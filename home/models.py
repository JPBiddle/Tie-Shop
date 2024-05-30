from django.db import models
import datetime


# Category of product
class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    name = models.CharField(max_length=90)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    # Foreign key for category, enable it to be cascade deleted, set category to default first category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, default='')
    # Set description to 750 chars, enabled to be empty and empty by default
    description = models.CharField(max_length=750, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    image_2 = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name

