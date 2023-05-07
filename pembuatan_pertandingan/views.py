from django.shortcuts import render

# Create your views here.
def list_pertandingan(request) :
    return render(request, 'list_pertandingan.html')

def pilih_stadium_tanggal(request) :
    return render(request, 'pilih_stadium_tanggal.html')