from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about", views.about, name='about'),
    path("schools",views.schools,name='schools'),
    path("contact",views.contact,name='contact'),
    path('details/<int:id>',views.details,name='details'),
    path('staff/<int:id>',views.staff,name='staff'),
    path('fees/<int:id>',views.fees,name='fees'),
    path('city/<city>',views.city, name="city"),
]