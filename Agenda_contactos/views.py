from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.forms import Form
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . models import contacto
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    username = request.POST['txtusuario']
    password = request.POST['txtpassword']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, f'Bienvenido {username}')
        return redirect('home')
    else:
        messages.warning(request, 'Usuario o contraseña incorrecta')
        return redirect('inicio')


def registrarse(request):
    nombre = request.POST['txtnombre']
    email = request.POST['txtemail']
    password = request.POST['txtpassword']
    password2 = request.POST['txtpassword2']
    usename_exists = User.objects.filter(username=nombre).exists()
    if usename_exists:
        messages.warning(request, 'El usuario ya existe')
    else:
        if nombre == '' or email == '' or password == '' or password2 == '':
            messages.warning(request, 'Existen campos vacios')
        else:
            if password == password2:
                usuario_nuevo = User.objects.create_user(nombre, email, password)
                usuario_nuevo.save()
                mensaje = f'Bienvenido {usuario_nuevo.username} ahora solo queda iniciar sesión'
                messages.success(request, mensaje)
                redirect('home')
            else:
                mensaje = 'Las contraseñas no coinciden'
                messages.error(request, mensaje)
    return redirect('inicio')
    
@login_required
def home(request):
    nombrebus = request.GET.get('txtbuscar', False)
    if nombrebus == False:
        contactosEncontrados = contacto.objects.filter(usuario_id = auth.get_user(request).id ).order_by('nombre')    
    else:
        contactosEncontrados = contacto.objects.filter(nombre__contains=nombrebus, usuario_id = auth.get_user(request).id).order_by('nombre')  
        if len(contactosEncontrados) == 0:
            mensaje = nombrebus + ' no existe'
            messages.warning(request, mensaje)
    return render(request,"crud.html",{"contacto": contactosEncontrados})
    

@login_required
def crearcontacto(request):
    nombre = request.POST['txtnombre'].capitalize()
    apellido = request.POST['txtapellido'].capitalize()
    telefono = request.POST['txttelefono']
    email = request.POST['txtemail']

    if nombre == '' or apellido == '' or email == '' or telefono == 0:
        messages.warning(request, 'Existen campos vacios')
    else:
        contacto_nuevo = contacto.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, email=email, usuario_id=request.user.id)
        texto = '{} ha sido creado'
        messages.success(request, texto.format(nombre))
    return redirect('home')

@login_required
def edicioncontacto(request,id):
    contacto_edit = contacto.objects.get(id=id)
    return render(request,"edicioncontacto.html",{"id": contacto_edit})


@login_required
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
        return redirect('home')

@login_required
def eliminarcontacto(request,id):
    contacto_elim = contacto.objects.get(id=id)
    contacto_elim.delete()
    texto = '{} ha sido eliminado'
    messages.success(request, texto.format(contacto_elim.nombre))
    return redirect('home')





