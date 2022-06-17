from django import forms
from django.forms import ModelForm
from .models import mascota,producto,cliente,compra

class mascotasForms(ModelForm):         #---------->El parentesis tiene que ir con ModelForm pedaso de cono
    
    class Meta:
        model=mascota
        fields = ['raza','peso','estatura','annos_de_vida','precio']
        
        label={
            'raza':'Raza',
            'peso':'Peso',
            'estatura':'Estatura',
            'annos_de_vida':'Años_de_vida',
            'precio':'pesos'    
        }
        Widgets={
            'raza':forms.TextInput(attrs={'class':'from-control'}),
            'peso':forms.TextInput(attrs={'class':'from-control'}),
            'estatura':forms.TextInput(attrs={'class':'from-control'}),
            'annos_de_vida':forms.TextInput(attrs={'class':'from-control'}),
            'precio':forms.TextInput(attrs={'class':'from-control'}),
        }

class productosForms(ModelForm):
    class Meta:
        model=producto
        fields=['codigo','nombre','cantidad','precio']
        
        label={
            'codigo':'Codigo',
            'nombre':'Nombre',
            'cantidad':'Cantidad',
            'precio':'Precio'
        }
        Widgets={
            'codigo':forms.TextInput(attrs={'class':'from-control'}),
            'nombre':forms.TextInput(attrs={'class':'from-control'}),
            'cantidad':forms.TextInput(attrs={'class':'from-control'}),
            'precio':forms.TextInput(attrs={'class':'from-control'}),
        }

    
class clienteForms(ModelForm):
    class Meta:
        model= cliente
        fields=['rut','nombre','edad','correo','telefono']
        
        label={
            'rut':'Rut',
            'nombre':'Nombre',
            'edad':'Edad',
            'correo':'Correo',
            'telefono':'Telefono',
        }
        
        Widgets={
            'rut':forms.TextInput(attrs={'class':'from-control'}),
            'nombre':forms.TextInput(attrs={'class':'from-control'}),
            'edad':forms.TextInput(attrs={'class':'from-control'}),
            'correo':forms.TextInput(attrs={'class':'from-control'}),
            'telefono':forms.TextInput(attrs={'class':'from-control'}),
        }