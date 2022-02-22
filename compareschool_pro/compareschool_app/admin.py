from django.contrib import admin
from compareschool_app.models import  Admission, Admission_Form, Images, Performance, SchoolDetail,Staff,Fees, User
from django.utils.html import format_html
# Register your models here.

@admin.register(SchoolDetail)
class SchoolDetailAdmin(admin.ModelAdmin):
    list_display = ('Name','Established','Image1','Website')
    search_fields = ['Name']
    # readonly_fields = ('Image1','Image2','Image3','Image4','Image5')
    list_filter = ['Name']
    list_display_links = ['Name']
    list_per_page = 10

    def Image1(self,obj):
        return format_html(f"<img src = '/media/{obj.image}style='height:200px;width:200px>")
    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('Name','Designation')
    search_fields = ('Name','Designation')
    # readonly_fields = ['Image']
    list_filter = ['Designation']
    list_display_links = ["Name"]
    list_per_page = 10

    def Image(self, obj):
        return format_html(f"<img src = '/media/{obj.image}style='height:200px;width:200px>")

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = ['FeesSchoolName','Standard','Batch','Medium']
    search_fields = ['FeesSchoolName']
    list_filter = ('Standard','Medium','Batch')
    list_display_links = ['FeesSchoolName']
    list_per_page = 10

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','mobile']
    search_fields = ['email']
    list_display_links = ['email']
    
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['ImagesSchoolName']
    search_fields = ['ImagesSchoolName']

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['PerformanceSchoolName']
    search_fields = ['PerformanceSchoolName']

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['AdmissionSchoolName']
    search_fields = ['AdmissionSchoolName']

@admin.register(Admission_Form)
class Admission_FormAdmin(admin.ModelAdmin):
    list_display = ['First_Name','Last_Name','Email','DOB']
    # search_fields = ['AdmissionformSchoolName']





