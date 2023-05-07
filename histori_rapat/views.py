from django.shortcuts import render

def histori_rapat(request):
    context = {}
    return render(request, 'show_histori.html', context)