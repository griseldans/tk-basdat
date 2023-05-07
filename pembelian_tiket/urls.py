from django.urls import path
from pembelian_tiket.views import *

urlpatterns = [
    path('list-pertandingan/', list_pertandingan, name='beli_tiket_list_pertandingan'),
    path('beli-tiket/', beli_tiket, name='beli_tiket')
]