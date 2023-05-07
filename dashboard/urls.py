from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('manager/', views.show_dashboard_manager, name='show_dashboard_manager'),
    path('panitia/', views.show_dashboard_panitia, name='show_dashboard_panitia'),
    path('penonton/', views.show_dashboard_penonton, name='show_dashboard_penonton'),
]
