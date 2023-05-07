"""
URL configuration for U_LEAGUE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('peminjaman_stadium/', include('peminjaman_stadium.urls')),
    path('mng_kelola_tim/', include('mng_kelola_tim.urls')),
    path('mulai_pertandingan/', include('mulai_pertandingan.urls')),
    path('mulai_rapat/', include('mulai_rapat.urls')),
    path('histori_rapat/', include('histori_rapat.urls')),
    path('register/', include('register_pengguna.urls')),
    path('pembuatan-pertandingan/', include('pembuatan_pertandingan.urls')),
    path('pembelian-tiket/', include('pembelian_tiket.urls')),
]
