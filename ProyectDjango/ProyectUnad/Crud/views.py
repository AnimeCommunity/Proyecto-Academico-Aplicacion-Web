from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

#CRUD

def Tienda(request):
    productos = Producto.objects.all()
    #categorias = Categoria.objects.all()
    

    return render(request, 'index.html', {'productos': productos})

#CREAR

def crear(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']  
        disponible = request.POST['disponible']
        

        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            categoria=categoria,
            disponible=disponible,
        )
    return redirect('Tienda')

#ELIMINAR - JHON

def eliminar(request, id):
    producto.objects.filter(id=id).delete()

    return redirect('Tienda')
 


#LEER - FELIPE/HTML
#ACTUALIZAR - FABIO

def actualizar_producto(request, producto_id):
    producto_obj = get_object_or_404(producto, id=producto_id)

    if request.method == "POST":
        
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        
        disponible = request.POST['disponible']
        categoria_id = request.POST['categoria']  


        # Buscar el producto y actualizarlo
        producto_obj.save()

    return redirect('Tienda')  


#TODO - SANTIAGO


