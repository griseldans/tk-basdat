from django.urls import path
from register_pengguna.views import *

urlpatterns = [
    path('', register_opsi_role, name='register_opsi_role'),
    path('manajer-penonton/', register_manajer_penonton, name='register_manajer_penonton'),
    path('panitia/', register_panitia, name='register_panitia')
]
