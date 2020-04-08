from django.db import models

# Create your models here.

class Contry(models.Model):
    name_contry=models.CharField(max_length=50)
    def __str__(self):
        return self.name_contry

class City(models.Model):
    name_city=models.CharField(max_length=50)
    clé_contry=models.ForeignKey(Contry,on_delete=models.CASCADE)
    def __str__(self):
        return self.name_city
    
class Aeroport(models.Model):
    name_aeroport=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    altitude=models.CharField(max_length=200)
    # timezone1=models.IntegerField()
    # timezone2=models.IntegerField()
    clé_city=models.ForeignKey(City,on_delete=models.CASCADE)
    clé_contry=models.ForeignKey(Contry,on_delete=models.CASCADE)

    
    
class Airline(models.Model):
    name_airline=models.CharField(max_length=200)
    clé_contry=models.ForeignKey(Contry,on_delete=models.CASCADE)
    def __str__(self):
        return self.name_airline

class Plane(models.Model):
    name_plane=models.CharField(max_length=200)
    code_iata=models.CharField(max_length=20)
    code_oaci=models.CharField(max_length=20)
    def __str__(self):
        return self.name_plane
    
class Ligne(models.Model):
    clé_airline=models.ForeignKey(Airline,on_delete=models.CASCADE)
    clé_aeroport_dep=models.ForeignKey(Aeroport,on_delete=models.CASCADE)
    clé_aeroport_arr=models.ForeignKey(Aeroport,related_name="aeroportarr",on_delete=models.CASCADE)
    arrete=models.CharField(max_length=20)
    type_avion=models.CharField(max_length=200)