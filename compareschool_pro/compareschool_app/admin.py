from django.contrib import admin
from compareschool_app.models import SchoolDetail,Staff,Fees
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
    list_display = ('Standard','Medium','Batch','Fees')
    search_fields = ('Standard','Medium')
    list_filter = ('Standard','Medium','Batch')
    list_display_links = ['Standard']
    list_per_page = 10



