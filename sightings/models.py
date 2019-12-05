from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField()

    longitude = models.FloatField()

    squirrel_id = models.CharField(max_length=20,primary_key=True,help_text=_("Unique Squirrel ID. If the ID already exist, sighting won't be added"),)

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        default=AM,
        help_text=_("Sighting session"),
    )

    date = models.DateField("Date")

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    
    AGE_CHOICES = (
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
        ('',''),
    )
    
    age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES,
        default=ADULT,
        help_text=_("Age of Squirrel"),
        null=True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    
    FUR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
        ('',''),
    )
    
    fur_color = models.CharField(
        max_length=20,
        choices=FUR_CHOICES,
        default=GRAY,
        help_text=_('Fur color of Squirrel'),
        null=True
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    

    LOC_CHOICES = (
        (GROUND_PLANE,'Ground Plane'),
        (ABOVE_GROUND,'Above Ground'),
        ('',''),
    )

    location = models.CharField(
        max_length=30,   
        choices=LOC_CHOICES,
        default=GROUND_PLANE,
        help_text=_("Location of Squirrel"),
        null=True,
    )

    specific_location = models.CharField(max_length=200,help_text=_("Specific location of Squirrel"), null=True, blank=True,)
    running = models.BooleanField(default=False,)
    chasing = models.BooleanField(default=False,)
    climbing = models.BooleanField(default=False,)
    eating = models.BooleanField(default=False,)
    foraging = models.BooleanField(default=False)
    other_activities = models.CharField(max_length=200, null=True, blank=True, help_text=_("Other Activity"),)
    kuks = models.BooleanField(default=False,)
    quaas = models.BooleanField(default=False,)
    moans = models.BooleanField(default=False,)
    tail_flags = models.BooleanField(default=False,)
    tail_twitches = models.BooleanField(default=False,)
    approaches = models.BooleanField(default=False,)
    indifferent = models.BooleanField(default=False,)
    runs_from = models.BooleanField(default=False,)

    def __str__(self):
        return self.squirrel_id

# Create your models here.
