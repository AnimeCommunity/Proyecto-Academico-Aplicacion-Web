from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Crud, name='index'),
    path('delete/<int:id>' , views.eliminar, name='eliminar'),
  
    
]
