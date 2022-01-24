import mimetypes
# from msilib.schema import File
from os import path
from tokenize import Name
from django.core.checks import messages
from django.db import connection
from django.http import Http404, HttpResponse, response
from django.shortcuts import redirect, render
from platformdirs import os
from .models import  Fees, Images, Performance, SchoolDetail, Staff, Fees, User
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Create your views here.

def index(request):
    detail = SchoolDetail.objects.all().order_by('-Date')
    school = SchoolDetail.objects.count()
    return render(request, "Home.html",{'detail':detail, 'school':school})

def about(request):
    school = SchoolDetail.objects.count()
    return render(request, "about.html",{'school':school})

def schools(request):
    if not 'userid' in request.session:
        # messages.success(request, 'Login Required')
        return redirect("login")
    else:
        school = SchoolDetail.objects.all() 
        return render(request,'schools.html',{'school':school})


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search/')
        post1 = SchoolDetail.objects.all().filter(City=search)
        return render(request, 'searchbar.html',{'post1':post1})

def contact(request):
    return render(request,'contact.html')

def details(request, id, performanceid):
    detail = SchoolDetail.objects.get(id=id)
    performance = Performance.objects.filter(PerformanceSchoolName__id=performanceid)
    return render(request,'school-details.html',{'detail':detail,'performance' : performance})

def staff(request,id):
    staffdetail = Staff.objects.filter(SchoolName__id=id)
    return render(request,'staff.html',{'staffdetail':staffdetail})

def fees(request,id):
    feesdetail = Fees.objects.filter(FeesSchoolName__id=id)
    return render(request,'fees.html',{'feesdetail':feesdetail})

def city(request,city):
    citydetail = SchoolDetail.objects.filter(City=city)
    return render(request,'city.html',{'citydetail': citydetail})

def images(request,id):
    schoolimages = Images.objects.filter(ImagesSchoolName__id=id)
    return render(request,'images.html',{'schoolimages' : schoolimages})

def download_file(id,request):
    try:
        file = SchoolDetail.objects.values_list('broucher',id=id)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = file
        filepath = BASE_DIR + '/media/files/' +filename
        path = open(filepath, 'rb')
        mime_type, _= mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

    except SchoolDetail.DoesNotExist:
        raise Http404

   

def login(request):
    if request.method == "POST":
        email = request.POST["txtemail"]
        user_given_password = request.POST["txtpassword"]
        count = User.objects.filter(email=email).count()
        if count == 1 :
            hashed_password = User.objects.only("password").get(email=email).password
            try:
                password_hasher = PasswordHasher()
                if password_hasher.verify(hashed_password, user_given_password) == True:
                    id = User.objects.only("id").get(email=email).id
                    request.session["userid"] = id
                    return redirect("/")
            except VerifyMismatchError:
                return render(request, "login.html", {"message" : "Invalid Email id or Password"})
        else:
            return render(request, "login.html",{"message" : "Invalid Email id or Password"})
    else:
        if not 'message' in request.session:
            return render(request, 'login.html')
        else:
            message = request.session["message"]
            del request.session["message"]
            return render(request,'login.html',{'message':message})


def register(request):
    if request.method == "POST":
        email = request.POST['txtemail']
        mobile = request.POST['txtmobile']
        password = request.POST['txtpassword']
        confirm_password = request.POST['txtconfirmpassword']
        if password != confirm_password:
            return render(request, "register.html",{"message" : "Confirm Password does not match to the Password."})
        else:
            email_count = User.objects.filter(email=email).count()
            mobile_count = User.objects.filter(mobile=mobile).count()
            if email_count>=1 or mobile_count>=1:
                return render(request, "register.html", {'message' : 'Email or Mobile is already registered with us!'})
            else:
                password_hasher = PasswordHasher()
                hashed_password = password_hasher.hash(password)
                with connection.cursor() as cursor:
                    cursor.execute("insert into compareschool_app_user (email,password,mobile) values (%s,%s,%s)", [email, hashed_password, mobile])
                    cursor.close()
                    request.session["message1"] = "Register Successfully"
                # messages.success(request, 'Register Successfully')
                return redirect("login")
    return render(request, "register.html")    



def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')
        