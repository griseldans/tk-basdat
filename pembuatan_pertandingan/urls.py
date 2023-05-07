from django.urls import path
from pembuatan_pertandingan.views import *

urlpatterns = [
    path('', list_pertandingan, name='list_pertandingan'),
    path('pilih-stadium-tanggal/', pilih_stadium_tanggal, name='pilih_stadium_tanggal')
]