from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from Agenda_contactos.views import * 
from Notitas.views import *

urlpatterns = [
    path('lista_notas',NotasListView.as_view(),name='lista_notas'),
    path('crear_nota',NotasCreateView.as_view(),name='crear_nota'),
    path('accounts/',include('django.contrib.auth.urls')),
    ]