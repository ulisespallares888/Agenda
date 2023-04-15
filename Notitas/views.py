
from django.contrib.messages.api import success
from django.http import request,HttpResponse
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
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@method_decorator(login_required, name='dispatch')
class NotasListView(ListView):
    model = notitas
    template_name = 'crud_notitas.html'
    context_object_name = 'notatias'

    def get_queryset(self):
        return notitas.objects.filter(propietario_id = self.request.user.id).order_by('fecha_creacion').reverse()
    
    
##### views.py #####
@login_required
def crear_nota(request):
    titulo = request.POST['texttitulo']
    contenido = request.POST['textcontenido']
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

@csrf_exempt
@login_required
def editar_nota(request,id_nota):
    titulo = request.POST.get('recipient-name',False)  
    contenido = request.POST.get('message-text',False)
    if titulo == "" or contenido == "":
        messages.warning(request, 'Existen campos vacios')
        return redirect('lista_notas')
    else:

        nota_edit = notitas.objects.get(id=id_nota)
        nota_edit.titulo = titulo
        nota_edit.contenido = contenido
        nota_edit.save()
        messages.success(request, "Modificación exitosa")
        return redirect('lista_notas')

"""@login_required
def editarcontacto(request,id):
    nombre = request.POST['txtnombre'].capitalize()
    apellido = request.POST['txtapellido'].capitalize()
    telefono = request.POST['txttelefono']
    email = request.POST['txtemail']
    if nombre == '' or apellido == '' or email == '' or telefono == 0:
        messages.warning(request, 'Existen campos vacios')
        contacto_edit = contacto.objects.get(id=id)
        return render(request,"edicioncontacto.html",{"id": contacto_edit})
        
    else:
        contacto_edit = contacto.objects.get(id=id)
        contacto_edit.nombre = nombre
        contacto_edit.apellido = apellido
        contacto_edit.telefono = telefono
        contacto_edit.email = email
        contacto_edit.save()
        texto = '{} ha sido actualizado'
        messages.success(request, texto.format(contacto_edit.nombre))
        return redirect('home')"""
