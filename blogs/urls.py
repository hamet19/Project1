

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('plane/',views.showPlane),
    path('airline/',views.showAirline),
    path('aeroport/',views.showAeroport),
    path('ligne',views.showLigne),
    
]
