from django.shortcuts import render
from .models import Dessert

def home(request):
    prostrecitos = Dessert.objects.all()
    return render(request, 'core/index.html', {'postres': prostrecitos})