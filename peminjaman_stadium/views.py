from django.shortcuts import render

# Create your views here.
def daftar_peminjaman(request) :
    return render(request, 'daftar_peminjaman.html')

def peminjaman(request) :
    return render(request, 'peminjaman.html')

def list_waktu(request) :
    return render(request, 'list_waktu.html')
