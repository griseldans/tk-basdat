from django.shortcuts import render

# Create your views here.
def peminjaman_stadium(request) :
    return render(request, 'peminjaman_stadium.html')