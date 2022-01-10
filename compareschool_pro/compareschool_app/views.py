from django.shortcuts import render
from .models import Fees, SchoolDetail, Staff, Fees

# Create your views here.

def index(request):
    return render(request, "Home.html")

def about(request):
    return render(request, "about.html")

def schools(request):
    school = SchoolDetail.objects.all()
    return render(request,'schools.html',{'school':school})

def contact(request):
    return render(request,'contact.html')

def details(request, id):
    detail = SchoolDetail.objects.get(id=id)
    return render(request,'school-details.html',{'detail':detail})

def staff(request,id):
    staffdetail = Staff.objects.filter(SchoolName__id=id)
    return render(request,'staff.html',{'staffdetail':staffdetail})

def fees(request,id):
    feesdetail = Fees.objects.filter(FeesSchoolName__id=id)
    return render(request,'fees.html',{'feesdetail':feesdetail})

def city(request,city):
    citydetail = SchoolDetail.objects.filter(City=city)
    return render(request,'city.html',{'citydetail': citydetail})