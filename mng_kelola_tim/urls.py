from django.urls import path
from mng_kelola_tim.views import daftar_tim, detail_tim, daftar_pemain, daftar_pelatih
app_name = "mng_kelola_tim"

urlpatterns = [
    path('daftar-tim/', daftar_tim, name='daftar-tim'),
    path('detail-tim/', detail_tim, name='detail-tim'),
    path('daftar-pemain/', daftar_pemain, name='daftar-pemain'),
    path('daftar-pelatih/', daftar_pelatih, name='daftar_pelatih'),
]