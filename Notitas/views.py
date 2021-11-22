from django.forms import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.edit import  CreateView, UpdateView, DeleteView 
from django.views.generic import ListView
from .models import notitas
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class NotasListView(ListView):
    model = notitas
    template_name = 'crud_notitas.html'
    context_object_name = 'notatias'

@method_decorator(login_required, name='dispatch')
class NotasCreateView(CreateView):
    model = notitas
    fields = ['titulo', 'contenido','propietario']
    template_name = NotasListView.template_name
    success_url = reverse_lazy('lista_notas')






