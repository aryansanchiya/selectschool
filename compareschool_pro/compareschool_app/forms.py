from cProfile import label
from statistics import mode
from django import forms
from .models import Admission_Form

class Admissionform(forms.ModelForm):
    class Meta:
        model = Admission_Form
        fields = ['AdmissionformSchoolName','First_Name','Last_Name','Father_Name','Email','DOB','Std','Std_Per','Board']
        schoolname = forms.CharField(label='School Name', max_length=255).widget = forms.HiddenInput()
        firstname = forms.CharField(label='Enter First Name',max_length=255)
        lastname = forms.CharField(label='Enter Last Name',max_length=255)
        fathername = forms.CharField(label='Enter the Father Name',max_length=255)
        email = forms.EmailField(label='Enter the Email')
        dob = forms.DateField(label="Enter your Birth Date")
        std = forms.IntegerField(label='Enter The Standard in which you want admission')
        std_per = forms.IntegerField(label='Enter the Last Standard')
        board = forms.CharField(label='Enter the Board in which you want admission')