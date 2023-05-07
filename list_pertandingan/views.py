from django.shortcuts import render

# Create your views here.
def list_pertandingan_manager(request):
    return render(request, 'list_pertandingan_manager.html')

def list_pertandingan_penonton(request):
    return render(request, 'list_pertandingan_penonton.html')
