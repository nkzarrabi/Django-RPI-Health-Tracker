# inventory/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rugs/', views.rug_list, name='rug_list'),
    path('rugs/new/', views.rug_new, name='rug_new'),  # Add this line
    path('rugs/<int:pk>/', views.rug_detail, name='rug_detail'),
    path('rugs/<int:pk>/edit/', views.rug_edit, name='rug_edit'),
    path('rugs/<int:pk>/delete/', views.rug_delete, name='rug_delete'),
    path('search/', views.search, name='search'),
]
