from operator import mod
from statistics import mode
from django.db import models
from django.db.models.base import Model


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
    Image5 = models.ImageField(upload_to="media/pics")      #Hostell
    Mobile_No = models.IntegerField(default=None)
    Phone_No = models.IntegerField(default=None)
    Email = models.EmailField()
    Website = models.URLField(default=None)
    City = models.CharField(max_length=200)
    Date = models.DateField()
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
    Standard = models.IntegerField()
    Medium = models.CharField(max_length=40)
    Batch = models.CharField(max_length=100)
    Fees = models.IntegerField()

    def __str__(self):
        return self.Medium

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=32)

   
