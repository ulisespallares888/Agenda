from django.contrib import admin
from django.urls import path
from Agenda_contactos import views 

urlpatterns = [
    path('',views.home),
    path('index/registrarse/',views.registrarse),
    path('index/',views.index),
    path('crearcontacto/',views.crearcontacto,name='crearcontacto'),
    path('eliminarcontacto/<id>',views.eliminarcontacto,name='crearcontacto'),
    path('edicioncontacto/<id>',views.edicioncontacto,name='crearcontacto'),
    path('editarcontacto/<id>',views.editarcontacto,name='crearcontacto'),
    path('index/iniciar_sesion/',views.iniciar_sesion,name='iniciar_sesion/')
    ]