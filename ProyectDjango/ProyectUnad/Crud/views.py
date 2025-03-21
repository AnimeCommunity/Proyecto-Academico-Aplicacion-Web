from django.shortcuts import render

def Crud(request):
    return render(request, 'index.html')

def sectionOne(request):
    return render(request, 'sectionOne.html')