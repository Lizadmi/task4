from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal-list'),
    path('edit/<int:pk>/', views.animal_edit, name='animal-edit'),
    path('delete/<int:pk>/', views.animal_delete, name='animal-delete'),
]
