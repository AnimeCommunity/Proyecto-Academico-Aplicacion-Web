from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Crud, name='index'),
    path('sectionOne.html/' , views.sectionOne, name='sectionOne'),
    
]
