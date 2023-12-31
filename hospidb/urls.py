from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('edit/<str:id>/', views.edit, name='edit')
]