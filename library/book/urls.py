# book/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_create, name='book_add'),
    path('<int:pk>/edit/', views.book_update, name='book_edit'),
]
