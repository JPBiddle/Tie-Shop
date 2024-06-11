from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_info, name='product_info'),
    path('colour/<str:blub>', views.colour, name='colour'),
    path('category/<str:plob>', views.category, name='category'),
]
