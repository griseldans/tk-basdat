from django.urls import path
from histori_rapat.views import histori_rapat
app_name = "histori_rapat"

urlpatterns = [
    path('', histori_rapat, name='histori_rapat'),
]