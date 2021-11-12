from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from Agenda_contactos import views 

urlpatterns = [
    path('home',views.home,name='home'),
    path('accounts/login/registrarse/',views.registrarse),
    path('',views.index, name='index'),
    path('crearcontacto/',views.crearcontacto,name='crearcontacto'),
    path('eliminarcontacto/<id>',views.eliminarcontacto,name='eliminarcontacto'),
    path('edicioncontacto/<id>',views.edicioncontacto,name='edicioncontacto'),
    path('editarcontacto/<id>',views.editarcontacto,name='editarcontacto'),
    #path('',views.index,name=''),
    #path('cerrar_session/',views.cerrar_session,name='cerrar_sesion'),
    path('accounts/',include('django.contrib.auth.urls')),
    ]