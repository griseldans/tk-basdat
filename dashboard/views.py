from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_dashboard_panitia(request):
    return render(request, 'dash_panitia.html')

def show_dashboard_manager(request):
    return render(request, 'dash_manager.html')

def show_dashboard_penonton(request):
    return render(request, 'dash_penonton.html')

# render(request, "dash_manager.html")