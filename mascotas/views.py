from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post,mascota,producto,cliente,compra
from .forms import mascotasForms,productosForms,clienteForms

#------Codigo de las mascotas.................................
def home(request):
    return render(request, "mascotas/index_base.html")

def cli(request):
    return render(request, "mascotas/listar_clie.html")

def listar_mascotas(request):
    mascotas=mascota.objects.all()
    data={
        'mascotas':mascotas
    }
    return render(request,"mascotas/listar_mascotas.html",data)

def agregar_mascota(request):
    data={"form":mascotasForms}
    if request.method == "POST":
        form = mascotasForms(request.POST)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.save()
            return redirect(agregar_mascota)
    else:
        return render(request,"mascotas/agregar_mascota.html",data)

def modificar_mascota(request,id):
    mascotas=get_object_or_404(mascota,id=id)
    data={
        'form':mascotasForms(instance=mascotas)
    }
    if request.method=="POST":
        form=mascotasForms(data=request.POST,instance=mascotas,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(listar_mascotas)
    return render(request,"mascotas/editar_mascota.html",data)

def eliminar(request,id):
    eliminar=get_object_or_404(mascota,id=id)
    eliminar.delete()
    return redirect(listar_mascotas)
#--------------------Termino el codigo de las mascotas..............
#...................................................................
#--------------------Inicio del codigo de productos-----------------
def agregar_prod(request):
    data={"form":productosForms}
    if request.method=="POST":
        form=productosForms(request.POST)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.save()
            return redirect(agregar_prod)
    else:
        return render(request,"mascotas/agregar_prod.html",data)

def listar_prod(request):
    productos=producto.objects.all()
    data={
        'productos':productos
    }
    return render(request,"mascotas/listar_prod.html",data)

def modificar_prod(request,id):
    mascotas=get_object_or_404(producto,id=id)
    data={
        'form':productosForms(instance=mascotas)
    }
    if request.method=="POST":
        form=productosForms(data=request.POST,instance=mascotas,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(listar_prod)
    return render(request,"mascotas/editar_prod.html",data)
    

def eliminar_prod(request,id):
    eliminar=get_object_or_404(producto,id=id)
    eliminar.delete()
    return redirect(listar_prod)
#--------------------Termino el codigo de los productos.............
#...................................................................
#--------------------Inicio del codigo de cliente-------------------

def agregar_cliente(request):
    data={"form":clienteForms}
    if request.method == "POST":
        form = clienteForms(request.POST)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.save()
            return redirect(agregar_cliente)
    else:
        return render(request,"mascotas/agregar_cliente.html",data)

def listar_clie(request):
    clientes=cliente.objects.all()
    data={
        'clientes':clientes
    }
    return render(request,"mascotas/listar_clie.html",data)

def modificar_clie(request,id):
    mascotas=get_object_or_404(cliente,id=id)
    data={
        'form':clienteForms(instance=mascotas)
    }
    if request.method=="POST":
        form=clienteForms(data=request.POST,instance=mascotas,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(listar_clie)
    return render(request,"mascotas/editar_clie.html",data)
    

def eliminar_clie(request,id):
    eliminar=get_object_or_404(cliente,id=id)
    eliminar.delete()
    return redirect(listar_clie)