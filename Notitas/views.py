from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import notitas
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

"""def notes_list(request):
    return render(request, 'crud_notitas.html')"""
@method_decorator(login_required, name='dispatch')
class NotasListView(ListView):
    model = notitas
    template_name = 'crud_notitas.html'
    context_object_name = 'notatias'

"""class NotasCreateView(CreateView):
    model = notitas
    fields = ['title', 'description']
    template_name = 'create_notitas.html'
    success_url = '/'"""




