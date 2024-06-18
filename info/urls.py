from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.subject, name='faq'),
    path('add/', views.add_faq, name='add_faq'),
]