from django.shortcuts import render

# Create your views here.
def mulai_pertandingan(request) :
    return render(request, 'mulai_pertandingan.html')

def pilih_peristiwa(request) :
    return render(request, 'pilih_peristiwa.html')

