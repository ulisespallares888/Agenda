from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contacto,usuario
from django.contrib import messages

session=None


def index(request):
    return render(request,"index.html")


def cerrarsession(request):
    global session
    session = None
    return redirect("index")


def iniciar_sesion(request):
    nombre_usuario = request.POST['txtusuario']
    password = request.POST['txtpassword']
    usuario_sesion = usuario.objects.filter(nombre=nombre_usuario, password=password)
    
    if len(usuario_sesion) == 0:
        texto = 'El usuario y/o contraseña son incorrectas'
        messages.warning(request, texto)
    else:
        global session
        session = usuario_sesion[0].id
        print(session)
        texto = 'Bienvenido {}'
        messages.success(request, texto.format(usuario_sesion[0].nombre))
        return redirect('home')
    

def registrarse(request):
    nombre = request.POST['txtnombre']
    email = request.POST['txtemail']
    password = request.POST['txtpassword']
    password2 = request.POST['txtpassword2']

    if nombre == '' or email == '' or password == '' or password2 == '':
        messages.warning(request, 'Existen campos vacios')
    else:
        if password == password2:
            usuario_nuevo = usuario.objects.create(nombre=nombre, email=email, password=password)
            usuario_nuevo.save()
            session = usuario_nuevo
            texto = 'Bienvenido {}'
            messages.success(request, texto.format(nombre))
        else:
            texto = 'Las contraseñas no coinciden'
            messages.error(request, texto.format(nombre))
    return redirect('home')
    

def home(request):
    if session == None:
        return redirect("index")
    nombrebus = request.GET.get('txtbuscar', False)
    if nombrebus == False:
        contactosEncontrados = contacto.objects.filter(usuario_id = session ).order_by('nombre')
    else:
        contactosEncontrados = contacto.objects.filter(nombre__contains=nombrebus, usuario_id = session ).order_by('nombre')  
        if len(contactosEncontrados) == 0:
            mensaje = nombrebus + ' no existe'
            messages.warning(request, mensaje)
    return render(request,"crud.html",{"contacto": contactosEncontrados})
    


def crearcontacto(request):
    if session == None:
        return redirect('index')
    nombre = request.POST['txtnombre'].capitalize()
    apellido = request.POST['txtapellido'].capitalize()
    telefono = request.POST['txttelefono']
    email = request.POST['txtemail']

    if nombre == '' or apellido == '' or email == '' or telefono == 0:
        messages.warning(request, 'Existen campos vacios')
    else:
        contacto_nuevo = contacto.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, email=email, usuario_id=session)
        texto = '{} ha sido creado'
        messages.success(request, texto.format(nombre))
        
    return redirect('home')


def edicioncontacto(request,id):
    if session == None:
        return redirect('index')

    contacto_edit = contacto.objects.get(id=id)
    return render(request,"edicioncontacto.html",{"id": contacto_edit})

def editarcontacto(request,id):
    if session == None:
        return redirect('index')

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


def eliminarcontacto(request,id):
    if session == None:
        return redirect('index')

    contacto_elim = contacto.objects.get(id=id)
    contacto_elim.delete()
    texto = '{} ha sido eliminado'
    messages.success(request, texto.format(contacto_elim.nombre))
    return redirect('home')





