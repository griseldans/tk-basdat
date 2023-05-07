from django.shortcuts import render

def daftar_mulai_rapat(request):
    context = {}
    return render(request, 'daftar_mulai_rapat.html', context)

def daftar_isi_rapat(request):
    context = {}
    return render(request, 'daftar_isi_rapat.html', context)


