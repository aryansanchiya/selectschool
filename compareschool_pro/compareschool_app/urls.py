from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about", views.about, name='about'),
    path("schools",views.schools,name='schools'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path("contact",views.contact,name='contact'),
    path('details/<int:id>',views.details,name='details'),
    path('staff/<int:id>',views.staff,name='staff'),
    path('fees/<int:id>',views.fees,name='fees'),
    path('city/<city>',views.city, name="city"),
    path('images/<int:id>',views.images, name="images"),
    path('download/<int:id>/', views.download_file),
    path('login', views.login, name= 'login'),
    path('register', views.register, name='register'),
    # path('facalities/<int:id>',views.facalities, name="facalities"),
    path('logout', views.logout, name= 'logout')
]