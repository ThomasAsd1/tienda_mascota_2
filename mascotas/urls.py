from django.urls import path, include,re_path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('',views.cli,name='clie'),
    
    #---URLS de Listar-----------------------
    path('listar_mascota',views.listar_mascotas,name='listM'),
    path('listar_prod',views.listar_prod,name='listar_prod'),
    path('listar_clie',views.listar_clie,name='clie_list'),
    
    #---URLS de Agregar----------------------
    path('agregar_mascota',views.agregar_mascota,name='ag_mascota'),
    path('agregar_prod',views.agregar_prod,name='prod'),
    path('agregar_cli',views.agregar_cliente, name="clie"),
    
    #---URLS de Editar-----------------------
    path('editar_mascota/<id>/',views.modificar_mascota,name='editar_raza_id'),
    path('editar_prod/<id>/',views.modificar_prod,name='editar_prod_id'),
    path('editar_clie/<id>/',views.modificar_clie,name='editar_clie_id'),
    #--URLS de Eliminar----------------------
    path('eliminar/<id>/',views.eliminar,name='elimina_raza_id'),
    path('eliminar_prod/<id>/',views.eliminar_prod,name='elimina_prod_id'),
    path('eliminar_clie/<id>/',views.eliminar_clie,name='elimina_clie_id'),
]
