from django.shortcuts import render

# Create your views here.

def home(request):
    #page principal
    return render(request,'index.html')

def reservar(request):
    return render(request, 'reservar.html')

def planes(request):
    return render(request, 'planes.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')