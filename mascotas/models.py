from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    k= models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title

class producto(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    
    def __str__(self):
        return self.codigo
    
    
class cliente(models.Model):
    rut=models.CharField(max_length=15)
    nombre=models.CharField(max_length=120)
    edad=models.IntegerField()
    correo=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    
    def __str__(self):
        return self.rut
    
class mascota(models.Model):
    raza=models.CharField(max_length=20)
    peso=models.IntegerField()
    estatura=models.IntegerField()
    annos_de_vida=models.IntegerField()
    precio=models.IntegerField()
    
    def __str__(self):
        return self.raza
    
class compra(models.Model):
    rut=models.ForeignKey(cliente,null=False,blank=False,on_delete=models.CASCADE)
    raza=models.ForeignKey(mascota,null=False,blank=False,on_delete=models.CASCADE)
    nombre=models.ForeignKey(producto,null=False,blank=False,on_delete=models.CASCADE)
    precio=models.IntegerField()
    valar_pago=models.IntegerField()
    
    def __str__(self):
        return self.nombre