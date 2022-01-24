

from importlib.metadata import files
from pyexpat import model
from statistics import mode
from tokenize import blank_re
from django.db import models



# Create your models here.

class SchoolDetail(models.Model):
    Name = models.CharField(max_length=255)     
    Address = models.TextField()
    Established = models.DateField()
    Achievements = models.TextField()
    Hostel = models.CharField(max_length=100)
    Sports = models.CharField(max_length=255)
    Image1 = models.ImageField(upload_to="media/pics")      #Whole School
    Image2 = models.ImageField(upload_to = "media/pics")    #Campus
    Image3 = models.ImageField(upload_to="media/pics")      #Classroom     
    Image5 = models.ImageField(upload_to="media/pics")        #Hostell
        
    Mobile_No = models.IntegerField(default=None)
    Phone_No = models.IntegerField(default=None)
    Email = models.EmailField()
    Website = models.URLField(default=None)
    City = models.CharField(max_length=200)
    Date = models.DateField()
    Board = models.CharField(max_length=200)
    # Facilities
    Auditorium = models.CharField(max_length=200)
    Infirmary = models.CharField(max_length=200)
    Computer_lab = models.CharField(max_length=200)
    Science_lab = models.CharField(max_length=200)
    Library = models.CharField(max_length=200)
    Cafeteria = models.CharField(max_length=200)
    Hostel = models.CharField(max_length=200)
    Transportation = models.CharField(max_length=200)
    # activities
    Social_Developement = models.CharField(max_length=255)
    Picnic_Excursions = models.CharField(max_length=255)
    Physical = models.CharField(max_length=255)
    Cultural = models.CharField(max_length=255)
    Arts_Crafts = models.CharField(max_length=255)

    # file
    broucher = models.FileField(upload_to='files/', null=True, verbose_name="",blank=True)
    
    # Public Or Private
    Sector = models.CharField(max_length=100)

    # Performance
    
    
    
    def __str__(self):
        return self.Name


class Staff(models.Model):
    SchoolName = models.ForeignKey(SchoolDetail,on_delete=models.CASCADE, related_name="SchoolName",null=True)
    Name = models.CharField(max_length=255)
    Study_Carrier = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    Standard = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="media/pics")

    def __str__(self):
        return self.Name

class Fees(models.Model):
    FeesSchoolName = models.ForeignKey(SchoolDetail,on_delete=models.CASCADE, related_name="FeesSchoolName",null=True)
    Standard = models.CharField(max_length=200)
    Medium = models.CharField(max_length=40)
    Batch = models.CharField(max_length=100)
    Fees = models.IntegerField()

    def __str__(self):
        return self.Medium

class Images(models.Model):
    ImagesSchoolName = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE, related_name="ImagesSchoolName",null=True)
    # Campus Images
    Campus1 = models.ImageField(upload_to="media/pics",blank=True)  
    Campus2 = models.ImageField(upload_to="media/pics")  
    Campus3 = models.ImageField(upload_to="media/pics")
    # Class room images 
    Class1 = models.ImageField(upload_to="media/pics") 
    Class2 = models.ImageField(upload_to="media/pics") 
    Class3 = models.ImageField(upload_to="media/pics")
    # Lab Images
    Lab1 = models.ImageField(upload_to="media/pics") 
    Lab2 = models.ImageField(upload_to="media/pics") 
   # Other Buildings
    Area1 = models.ImageField(upload_to="media/pics") 
    Area2 = models.ImageField(upload_to="media/pics") 
    Area3 = models.ImageField(upload_to="media/pics")
    # Sports Ground
    Sports1 = models.ImageField(upload_to="media/pics") 
    Sports2 = models.ImageField(upload_to="media/pics") 
    Sports3 = models.ImageField(upload_to="media/pics")
    Sports4 = models.ImageField(upload_to="media/pics") 
    Sports5 = models.ImageField(upload_to="media/pics") 

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=32)

   
