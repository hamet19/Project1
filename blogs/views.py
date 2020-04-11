from django.shortcuts import render
from .models import *


# Create your views here.


def home(request):
    return render(request,'blogs/index.html')


def showPlane(request):
   
    name=request.POST.get('your_name',False)
    if not name:
         planes=Plane.objects.all()[:30]
    else:
        planes=Plane.objects.filter(name_plane__contains=name)
   
    return render(request,'blogs/plane.html',{'planes':planes,'your_name':name})

def showAirline(request):
    airlines=Airline.objects.all()
    return render(request,'blogs/airline.html',{'airlines':airlines})

def showAeroport(request):
    
    name=request.POST.get('your_name',False)
    if not name:
        aeroports=Aeroport.objects.all()[:30]
    else:
        contry=Contry.objects.get(name_contry=name)
        aeroports=Aeroport.objects.filter(clé_contry_id=contry.id)
    return render(request,'blogs/aeroport.html',{'aeroports':aeroports})   

     
def showLigne(request):
    return render(request,'blogs/ligne.html')
