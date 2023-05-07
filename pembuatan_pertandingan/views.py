from django.shortcuts import render

# Create your views here.
def  list_pertandingan(request):
    return render(request, 'list_pertandingan.html')

def  pilih_stadium_tanggal(request):
    return render(request, 'pilih_stadium_tanggal.html')

def jadwal_stadium(request):
    return render(request, 'jadwal_stadium.html')

def buat_pertandingan(request):
    return render(request, 'buat_pertandingan.html')