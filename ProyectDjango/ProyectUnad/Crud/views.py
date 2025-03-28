from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


#CRUD

def tienda(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.all()
    form = ProductoForm()

    if query:
        productos = productos.filter(nombre__icontains=query)
    

    #CREAR
    if request.method == 'POST':
         form = ProductoForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()
            return redirect("tienda")
              


    return render(request, 'index.html', {'productos': productos, "form":form, 'query': query})




#ELIMINAR - JHON
def eliminar (request, id):
    Producto.objects.filter(id=id).delete()
    return redirect('tienda')
 


#LEER - FELIPE/HTML
#ACTUALIZAR - FABIO
def actualizar(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("tienda")
    else:
        form = ProductoForm(instance=producto)
    

    return render(request, 'update.html', {"form":form, 'producto': producto}) 
         
 

         



#TODO - SANTIAGO



