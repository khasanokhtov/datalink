# datalens_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_dataset, name='create_dataset'),
    path('edit/<int:dataset_id>/', views.edit_dataset, name='edit_dataset'),
    path('delete/<int:dataset_id>/', views.delete_dataset, name='delete_dataset'),
    path('dataset/<int:dataset_id>/', views.dataset_detail, name='dataset_detail'),  # Это маршрут для страницы деталей датасета
    path('add_data/', views.add_data, name='add_data'),
]
    # Добавь другие маршруты здесь

