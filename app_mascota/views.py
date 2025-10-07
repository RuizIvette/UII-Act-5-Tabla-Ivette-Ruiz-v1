from django.shortcuts import render
from .models import Mascota
# Create your views here.
def index(request):
    mascotas= Mascota.objects.all()
    return render(request,'index.html',{'mascotas': mascotas})