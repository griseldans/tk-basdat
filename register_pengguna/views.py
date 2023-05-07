from django.shortcuts import render

# Create your views here.
def register_opsi_role(request) :
    return render(request, 'register_opsi_role.html')

def register_manajer_penonton(request) :
    return render(request, 'register_manajer_penonton.html')

def register_panitia(request) :
    return render(request, 'register_panitia.html')