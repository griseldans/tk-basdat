from django.urls import path
from mulai_rapat.views import daftar_mulai_rapat, daftar_isi_rapat
app_name = "mulai_rapat"

urlpatterns = [
    path('daftar-mulai-rapat/', daftar_mulai_rapat, name='daftar_mulai_rapat'),
    path('daftar-isi-rapat/', daftar_isi_rapat, name='daftar_isi_rapat'),
]