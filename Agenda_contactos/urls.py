from django.contrib import admin
from django.urls import path
from Agenda_contactos import views 

urlpatterns = [
    path('home',views.home,name='home'),
    path('registrarse/',views.registrarse),
    path('',views.index, name='index'),
    path('crearcontacto/',views.crearcontacto,name='crearcontacto'),
    path('eliminarcontacto/<id>',views.eliminarcontacto,name='eliminarcontacto'),
    path('edicioncontacto/<id>',views.edicioncontacto,name='edicioncontacto'),
    path('editarcontacto/<id>',views.editarcontacto,name='editarcontacto'),
    path('iniciar_sesion/',views.iniciar_sesion,name='iniciar_sesion/'),
    path('cerrarsession/',views.cerrarsession,name='cerrar_sesion'),

    ]