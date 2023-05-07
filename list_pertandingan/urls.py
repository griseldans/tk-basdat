from django.urls import path
from . import views

app_name = 'list_pertandingan'

urlpatterns = [
    path('manager/', views.list_pertandingan_manager, name='list_pertandingan_manager'),
    path('penonton/', views.list_pertandingan_penonton, name='list_pertandingan_penonton'),  
]
