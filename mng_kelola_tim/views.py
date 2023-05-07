from django.shortcuts import render

# Create your views here.
def daftar_tim(request):
    context = {}
    return render(request, 'daftar_tim.html', context)

def detail_tim(request):
    context = {}
    return render(request, 'detail_tim.html', context)

def daftar_pemain(request):
    context = {}
    return render(request, 'daftar_tim.html', context)

def daftar_pelatih(request):
    context = {}
    return render(request, 'daftar_pelatih.html', context)