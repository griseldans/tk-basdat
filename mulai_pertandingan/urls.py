from django.urls import path
from mulai_pertandingan.views import *

urlpatterns = [
    path('', mulai_pertandingan, name='mulai_pertandingan'),
    path('peristiwa/', pilih_peristiwa, name='pilih_peristiwa'),
    
]