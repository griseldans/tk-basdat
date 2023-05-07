from django.urls import path
from mng_kelola_tim.views import daftar_tim, detail_tim
app_name = "mng_kelola_tim"

urlpatterns = [
    path('daftar-tim/', daftar_tim, name='daftar-tim'),
    path('detail-tim/', detail_tim, name='detail-tim')
]