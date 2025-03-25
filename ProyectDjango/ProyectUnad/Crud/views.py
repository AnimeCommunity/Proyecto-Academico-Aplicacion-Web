from django.shortcuts import render, redirect, get_object_or_404
from .models import producto, categoria

def Crud(request):
    return render(request, 'index.html')

def actualizar_producto(request):
    if request.method == "POST":
        producto_id = request.POST.get('producto_id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')

        # Buscar el producto y actualizarlo
        producto_obj = get_object_or_404(producto, id=producto_id)
        producto_obj.nombre = nombre
        producto_obj.descripcion = descripcion
        producto_obj.precio = precio
        producto_obj.save()

        return redirect('index')  # Asegúrate de que esta URL está definida en urls.py

    return redirect('index')  # Si no es POST, regresa al CRUD


#CREAR - CAMILO
#ELIMINAR - JHON
#LEER - FELIPE/HTML
#ACTUALIZAR - FABIO
#TODO - SANTIAGO


