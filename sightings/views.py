from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from django.http import Http404

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'Squirrels': squirrels
            }
    return render(request, 'sightings/all.html', context)

def details(request, Unique_Squirrel_ID):
    try:
        squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    except Squirrel.DoesNotExist:
        raise Http404("Squirrel Does Not Exist")
    return render(request, 'sightings/details.html', {'squirrel': squirrel})


# Create your views here.
