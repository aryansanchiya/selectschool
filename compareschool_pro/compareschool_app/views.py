from ast import Pass
from email import message
from fileinput import close
import imp
import mimetypes
# from msilib.schema import File
from os import path
from tokenize import Name
from django.core.checks import messages
from django.db import connection
from django.forms import ValidationError
from django.http import Http404, HttpResponse, response
from django.shortcuts import redirect, render
from platformdirs import os

from .forms import Admissionform
from .models import  Admission, Admission_Form, Fees, Images, Performance, SchoolDetail, Staff, Fees, User
from argon2 import PasswordHasher, _password_hasher
from argon2.exceptions import VerifyMismatchError
import re
import string
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send_text_email(subject,message,receiver_email_list):
    sender_email = settings.EMAIL_HOST_USER
    send_mail( subject, message, sender_email, receiver_email_list )

def generate_random_password(length=16):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_password = ''
    for i in range(length):
        random_password= random_password +  random.choice(letters)
    return random_password

def index(request):
    detail = SchoolDetail.objects.all().order_by('-Date')
    school = SchoolDetail.objects.count()
    usermail = User.objects.values('email','id')
    performance = Performance.objects.all()
    return render(request, "Home.html",{'detail':detail, 'school':school,'usermail':usermail, 'performance' : performance})

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

def details(request, id, performanceid,admissionid):
    detail = SchoolDetail.objects.get(id=id)
    performance = Performance.objects.filter(PerformanceSchoolName__id=performanceid)
    admission = Admission.objects.filter(AdmissionSchoolName__id=admissionid)
    return render(request,'school-details.html',{'detail':detail,'performance' : performance, 'admission' : admission})

def admission_info(request,id):
    if request.method == 'POST':
        form = Admissionform(request.POST)
        schoolname = SchoolDetail.objects.values('Name').filter(id=id)
        if form.is_valid():
            admissionformschool = Admission_Form(AdmissionformSchoolName=schoolname)
            form.save()
            return redirect('/')
    admission_form = Admissionform()
    return render(request,"admission_form.html",{"form":admission_form})




    # # admissionformname= Admission.objects.values('AdmissionSchoolName')
    # admissionformschool.save()
    # if request.method == "POST":
    #     First_Name = request.POST['txtfname']
    #     Last_Name = request.POST['txtlname']
    #     Father_Name = request.POST['txtfathername']
    #     Email = request.POST['txtmail']
    #     DOB = request.POST['dob']
    #     Std = request.POST['std'] 
    #     Std_Per = request.POST['per']
    #     Board = request.POST['txtboard']
       
        
        # with connection.cursor() as cursor:
        #     cursor.execute("insert into compareschool_app_Admission_form(First_Name,Last_Name,Father_Name,Email,DOB,Std,Std_Per,Board) values (%s,%s,%s,%s,%s,%s,%s,%s)", 
        #     [First_Name,Last_Name,Father_Name,Email,DOB,Std,Std_Per,Board])
        #     cursor.close()
    return render(request, 'admission_form.html')
    
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
        firstname = request.POST['txtfname']
        lastname = request.POST['txtlname']
        email = request.POST['txtemail']
        mobile = request.POST['txtmobile']
        password = request.POST['txtpassword']
        confirm_password = request.POST['txtconfirmpassword']
        min_length = 7
        if len(password)<min_length:
             return render(request, "register.html", {'message' : 'PASSWORD MUST CONTAIN 7 LETTERS, ONE NUMERIC AND ONE CAPITAL LETTER!'})

        # if not any(char.isdigit() for char in password):
        #      return render(request, "register.html", {'message' : 'In Password must add One Numeric!'})
        
        if not re.search(r"[\d]+", password):            
            return render(request, "register.html", {'message' : 'PASSWORD MUST CONTAIN ONE NUMERIC'})

        if not re.search(r"[A-Z]+", password):
            return render(request, "register.html", {'message' : 'PASSWORD MUST CONTAIN MINIMUM ONE CAPITAL LETTER'})

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
                    cursor.execute("insert into compareschool_app_user (firstname,lastname,email,password,mobile) values (%s,%s,%s,%s,%s)", [firstname,lastname,email,hashed_password, mobile])
                    cursor.close()
                    request.session["message1"] = "Register Successfully"
                # messages.success(request, 'Register Successfully')
                return redirect("login")
    return render(request, "register.html") 

def forgotpassword(request):
    if request.method == "POST":
        email = request.POST['txtemail']
        count = User.objects.filter(email=email).count()
        if count == 0 :
            return render(request,'forgot-password.html',{"message":"Your Given Email is not Registered With Us!"})
        else:
            new_password = generate_random_password(7)

            password_hasher = PasswordHasher()
            hashed_password = password_hasher.hash(new_password)

            user = User.objects.get(email=email)
            user.password = hashed_password
            user.save()

            subject =  "Password Recovered!"
            message = f"Your Password Successfully Recovered. Your New Password is {new_password}"
            recipient_list = [email]
            send_text_email(subject,message,recipient_list)
            return redirect('/')
    return render(request, "forgot-password.html")

def changepassword(request):
    if not 'userid' in request.session:
        return redirect("/")
    if request.method == "POST":
        id = request.session["userid"]
        old_password = request.POST['txtcurrentpwd']
        new_password = request.POST['txtnewpwd']
        confirm_password = request.POST['txtcnfrmpwd']
        min_length = 7 
        if new_password != confirm_password:
            return render(request, "change_password.html",{'message1':"New Password and Confirm Password didn't match!"})

        if len(new_password)<min_length:
             return render(request, "change_password.html", {'message1' : 'PASSWORD MUST CONTAINS 7 LETTERS, ONE NUMERIC AND ONE CAPITAL LETTER!'})
        
        if not re.search(r"[\d]+", new_password):            
            return render(request, "change_password.html", {'message1' : 'PASSWORD MUST CONTAINS ONE NUMERIC'})

        if not re.search(r"[A-Z]+", new_password):
            return render(request, "change_password.html", {'message1' : 'PASSWORD MUST CONTAINS MINIMUM ONE CAPITAL LETTER'})

        else:
            hashed_password = User.objects.only('password').get(id=id).password

            try:
                password_hasher = PasswordHasher()
                if password_hasher.verify(hashed_password,old_password) == True:
                    user = User.objects.get(id=id)

                    hashed_password = password_hasher.hash(new_password)
                    user.password = hashed_password
                    user.save()
                    return redirect("logout")

            except VerifyMismatchError:
                return render(request,"change_password.html",{"message1":"Invalid Password"})
    return render(request, "change_password.html")

def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')
        