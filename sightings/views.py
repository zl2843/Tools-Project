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
    #return HttpResponse('Hi There')

def details(request, pk):
    try:
        squirrel = Squirrel.objects.get(pk=Unique_Squirrel_ID)
    except Squirrel.DoesNotExist:
        raise Http404("Squirrel Does Not Exist")
    return render(request, 'sightings/details.html', {'squirrel': squirrel})

def squirrel_map(request, template_name='sightings//map.html'):
    squirrels = Squirrel.objects.order_by('?')[:100]
    context = {
            'squirrels' : squirrels,
            }
    return render(request, template_name, context)

# Create your views here.
