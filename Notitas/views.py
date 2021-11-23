
from django.contrib.messages.api import success
from django.http import request,HttpResponse
from django.http.response import Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.edit import  CreateView, UpdateView, DeleteView 
from django.views.generic import ListView
from django.contrib.auth.models import User, auth
from .models import notitas
from django.contrib.auth import SESSION_KEY, authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@method_decorator(login_required, name='dispatch')
class NotasListView(ListView):
    model = notitas
    template_name = 'crud_notitas.html'
    context_object_name = 'notatias'

    def get_queryset(self):
        return notitas.objects.filter(propietario_id = self.request.user.id)
    
    
##### views.py #####
@login_required
def crear_nota(request):
    titulo = request.POST.get('texttitulo',False)
    contenido = request.POST.get('textcontenido',False)
    if titulo == '' or contenido == '':
        messages.warning(request, 'Existen campos vacios')
    else:
        nota_nueva = notitas.objects.create(titulo=titulo, contenido=contenido, propietario_id=auth.get_user(request).id)
        nota_nueva.save()
        messages.success(request, 'Nota creada')
    return redirect('lista_notas')

@login_required
def eliminar_nota(request, id_nota):
    nota = notitas.objects.get(id=id_nota)
    nota.delete()
    messages.success(request, 'Nota eliminada')
    return redirect('lista_notas')

"""
class crear_nota(CreateView):
    model = notitas
    fields = ['titulo','contenido']
    form = NotitasForm
    success_url = reverse_lazy('lista_notas')
    
    """

