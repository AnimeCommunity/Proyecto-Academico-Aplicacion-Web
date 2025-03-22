from django.shortcuts import render
from .models import producto, categoria

def Crud(request):
    return render(request, 'index.html')

#crud

def Tienda(request):
    categorias = categoria.objects.all()
    productos = producto.objects.all()

    return render(request, 'index.html', {'categorias': categorias, 'productos': productos})



#CREAR - CAMILO
#ELIMINAR - JHON
#LEER - FELIPE/HTML
#ACTUALIZAR - FABIO
#TODO - SANTIAGO


