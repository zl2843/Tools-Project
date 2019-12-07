from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    squirrel_id = models.CharField(max_length=20,primary_key=True,help_text=_("Gives Unique Squirrel ID. Sighting added only if the ID does not already exist"),)

    AM = 'AM'
    PM = 'PM'
    
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )
    
    latitude = models.FloatField(
            help_text=_('Gives the Latitude of Sighting'),
            )

    longitude = models.FloatField(
            help_text=_('Gives the Longitude of Sighting'),
            )
     

    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        default=AM,
        help_text=_("Gives the time of sighting occurence - AM or PM"),
    )

    date = models.DateField(help_text=_("Gives the date of sighting in YYYY-MM-DD format"),)

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
        help_text=_("Age of Squirrel - Adult or Juvenile"),
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
        help_text=_('Gives Fur color of the Squirrel'),
        null=True,
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
        help_text=_("Location of Squirrel - on ground plane or above ground plane"),
        null=True,
    )

    specific_location = models.CharField(max_length=200,help_text=_("Additional information on Specific location of the Squirrel"), null=True, blank=True,)
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
