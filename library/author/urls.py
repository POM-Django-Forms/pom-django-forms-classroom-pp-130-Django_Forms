from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.author_create, name='author_add'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/<int:pk>/edit/', views.author_update, name='author_edit'),
]
