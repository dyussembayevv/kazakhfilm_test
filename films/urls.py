from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
]
