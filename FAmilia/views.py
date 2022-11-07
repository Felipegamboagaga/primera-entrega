from django.shortcuts import render
from django.http import *
from  Familia.models import familia
from django.template import Template, context, loader

# Create your views here.
def fam(request):
    fam = familia.objects.all()
    context = {'fam': fam}
  
        
   

    return render(request, 'template.html', context)
    
    