from django.shortcuts import render, redirect
from .models import Dojos, Ninjas
# Create your views here.

def inicio(request):
    context = {
        "inicio": Dojos.objects.all()
    }
    return render(request, 'index.html', context)


