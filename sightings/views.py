from django.shortcuts import render

from django.http import HttpResponse
from .models import Squirrel

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'Squirrels': squirrels
            }
    return render(request, 'sightings/all.html', context)

def squirrels_details(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
    return HttpResponse('Hi, I am Squirrel {Unique_Squirrel_ID}')


# Create your views here.
