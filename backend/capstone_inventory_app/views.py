from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Propiedad, Usuario
from django.db import models
# def de funciones que manejan los http requests
# y retorna los http responses correspondientes


# views para las propiedades
def propiedad_list(request):
    propiedades = Propiedad.objects.all()
    data = {"propiedades": list(propiedades.values())}
    return JsonResponse(data)

# views para los detalles de una propiedad
def propiedad_detail(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    data = {"propiedad": {
        'tablilla': propiedad.tablilla,
        'color': propiedad.color,
        'num_serie': propiedad.num_serie,
        'cantidad': propiedad.cantidad,
        'localidad': propiedad.localidad,
        'fecha_de_adquisicion': propiedad.fecha_de_adquisicion,
        'propiedad_id': propiedad.propiedad_id,
        
        }
    }
     
    return JsonResponse(data)


def usuario_list(request, pk):
    usuarios = get_object_or_404(Propiedad, pk=pk)
    data = {
        'nombre': usuarios.nombre,
        'apellido': usuarios.apellido,
        'llave_usuario': usuarios.llave_usuario,
        'password': usuarios.password,
        'usuario_id': usuarios.usuario_id,
    }

    return JsonResponse(data)