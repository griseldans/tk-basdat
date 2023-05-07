from django.urls import path
from pembuatan_pertandingan.views import *

urlpatterns = [
    path('', list_pertandingan, name='list_pertandingan'),
    path('pilih-stadium-tanggal/', pilih_stadium_tanggal, name='pilih_stadium_tanggal'),
    path('jadwal_stadium/', jadwal_stadium, name='jadwal_stadium'),
    path('buat_pertandingan/', buat_pertandingan, name='buat_pertandingan'),
]