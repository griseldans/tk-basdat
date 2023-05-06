from django.urls import path
from peminjaman_stadium.views import *

app_name = 'peminjaman_stadium'

urlpatterns = [
    path('', peminjaman_stadium, name='peminjaman_stadium')
]