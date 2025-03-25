from django.urls import path
from . import views

urlpatterns = [
    path('' , views.tienda, name='tienda'),
    path('delete/<int:id>' , views.eliminar, name='eliminar'),
    path('actualizar/<int:id>' , views.actualizar, name='actualizar'),

  
    
]
