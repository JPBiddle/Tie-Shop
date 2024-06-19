from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.subject, name='faq'),
    path('add/', views.add_faq, name='add_faq'),
    path('delete/<int:question_id>/', views.delete_faq, name='delete_faq'),
    path('edit/<int:question_id>/', views.edit_faq, name='edit_faq'),
]