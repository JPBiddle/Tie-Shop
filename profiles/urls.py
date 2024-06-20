from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('wishlist/add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
    path('wishlist/remove_wishlist/<int:id>', views.remove_wishlist, name='remove_wishlist'),
]