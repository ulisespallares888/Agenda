from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from Agenda_contactos import views 

urlpatterns = [
    path('home',views.home,name='home'),
    path('accounts/login/registrarse/',views.registrarse),
    path('',views.inicio, name='inicio'),
    path('crearcontacto/',views.crearcontacto,name='crearcontacto'),
    path('eliminarcontacto/<id>',views.eliminarcontacto,name='eliminarcontacto'),
    path('edicioncontacto/<id>',views.edicioncontacto,name='edicioncontacto'),
    path('editarcontacto/<id>',views.editarcontacto,name='editarcontacto'),
    path('iniciar_sesion/',views.iniciar_sesion,name='iniciar_sesion'),
    path('accounts/',include('django.contrib.auth.urls')),
    ]