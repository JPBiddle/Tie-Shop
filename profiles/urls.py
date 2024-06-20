from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    # path('wishlist/', views.user_wishlist, name="user_wishlist"),
    path('wishlist/add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
]