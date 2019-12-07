from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from django.http import Http404
from .forms import SquirrelForm
from django.shortcuts import redirect

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels
            }
    return render(request, 'sightings/all.html', context)

def details(request, squirrel_id):
    squirrel = Squirrel.objects.get(pk=squirrel_id)
    return HttpResponse(squirrel.squirrel_id)

def edit_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(pk=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('sightings/')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
            'form': form
            }
    return render(request, 'sightings/edit.html', context)


def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings/')
    else:
        form = SquirrelForm()
    context = {
            'form': form,
            }
    return render(request, 'sightings/edit.html', context)

def squirrel_map(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels' : squirrels,
            }
    return render(request, 'sightings/map.html', context)

# Create your views here.
