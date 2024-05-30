from django.contrib import admin
from .models import Category, Product, Colour

admin.site.register(Category)
admin.site.register(Colour)
admin.site.register(Product)

