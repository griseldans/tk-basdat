from django.shortcuts import render

# Create your views here.
def list_pertandingan(request) :
    return render(request, 'pembelian_tiket_list_pertandingan.html')

def beli_tiket(request) :
    return render(request, 'pembelian_tiket_beli_tiket.html')