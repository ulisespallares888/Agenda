from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from Agenda_contactos import views 

urlpatterns = [
    path('home',views.home,name='home'),
    path('registrarse/',views.registrarse),
    path('',views.index, name='index'),
    path('crearcontacto/',views.crearcontacto,name='crearcontacto'),
    path('eliminarcontacto/<id>',views.eliminarcontacto,name='eliminarcontacto'),
    path('edicioncontacto/<id>',views.edicioncontacto,name='edicioncontacto'),
    path('editarcontacto/<id>',views.editarcontacto,name='editarcontacto'),
    path('',views.index,name=''),
    path('cerrarsession/',LogoutView.as_view(),name='cerrar_sesion'),
    ]