from django.shortcuts import render
from django.http import *
from  Familia.models import familia
from django.template import Template, context, loader

# Create your views here.
def fam(request):
    fam = familia.objects.all()
    fin = ""
    for miembro in fam:
        fin += f"({familia.nombre}, {familia.edad}, {familia.ultimo_log}"
        
   

    return render(request, 'template.html', {'fam':fam, 'fin':fin})
    
    