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
            return redirect('/sightings')
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
            return redirect('/sightings')
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

def stats(request):
    Number_of_Squirrels = Squirrel.objects.all().count()
    adult_squirrels = Squirrel.objects.filter(age='Adult').count()
    juvenile_squirrels = Squirrel.objects.filter(age='Juvenile').count()
    unknown_age = Squirrel.objects.filter(age='').count()
    gray_squirrels = Squirrel.objects.filter(fur_color='Gray').count()
    cinnamon_squirrels = Squirrel.objects.filter(fur_color='Cinnamon').count()
    black_squirrels = Squirrel.objects.filter(fur_color='Black').count()
    other_color = Squirrel.objects.filter(fur_color='').count()
    AM_Shift_squirrels = Squirrel.objects.filter(shift='AM').count()
    PM_Shift_squirrels = Squirrel.objects.filter(shift='PM').count()
    Location_ground = Squirrel.objects.filter(location='Ground Plane').count()
    Location_above = Squirrel.objects.filter(location='Above Ground').count()
    Location_unknown = Squirrel.objects.filter(location='').count()

    context = {
            'Number_of_squirrels': Number_of_Squirrels,
            'Number_of_adult_squirrels': adult_squirrels,
            'Number_of_juvenile_squirrels': juvenile_squirrels,
            'age_unknown': unknown_age,
            'Number_of_gray_squirrels': gray_squirrels,
            'Number_of_cinnamon_squirrels': cinnamon_squirrels,
            'Number_of_black_squirrels': black_squirrels,
            'other_color': other_color,
            'AM_Shift': AM_Shift_squirrels,
            'PM_Shift': PM_Shift_squirrels,
            'Ground_Plane': Location_ground,
            'Above_Ground': Location_above,
            'Unknown_location': Location_unknown,
            }

    return render(request, 'sightings/stat.html', context)

def home(request):
    return render(request, 'sightings/home.html')
# Create your views here.
