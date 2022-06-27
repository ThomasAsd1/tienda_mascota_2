from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone

import mascotas
from .models import Post,mascota,producto,cliente,compra
from .forms import mascotasForms,productosForms,clienteForms
# las importaciones para la API 
from rest_framework import generics
from .serializers import mascotaSerializer
#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import mascotaSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

@api_view(['GET', 'POST'])
def mascota_collection(request):
    if request.method == 'GET':
        mascotas = mascota.objects.all()
        serializer = mascotaSerializer(mascotas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = mascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mascota_element(request, pk):
    Mascota = get_object_or_404(mascota, id=pk)

    if request.method == 'GET':
        serializer = mascotaSerializer(Mascota)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        Mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        mascota_new = JSONParser().parse(request) 
        serializer = mascotaSerializer(Mascota, data=mascota_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
