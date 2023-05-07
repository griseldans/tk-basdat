from django.shortcuts import render

# Create your views here.
def daftar_tim(request):
    context = {}
    return render(request, 'daftar_tim.html', context)

def datail_tim(request):
    context = {}
    return render(request, 'detail_tim.html', context)