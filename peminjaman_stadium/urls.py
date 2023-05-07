from django.urls import path
from peminjaman_stadium.views import *

urlpatterns = [
    path('', daftar_peminjaman, name='daftar_peminjaman'),
    path('peminjaman/', peminjaman, name='peminjaman'),
    path('list_waktu/', list_waktu, name='list_waktu')
]
