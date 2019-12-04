from django.db import models

class Squirrel(models.Model):
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length=20,primary_key=True)

    AM = 'AM'
    PM = 'PM'
    Shift_Choices = (
        (AM, 'AM'),
        (PM, 'PM'),
    )
    Shift = models.CharField(
        max_length=2,
        choices=Shift_Choices,
    )

    Date = models.DateField("Date")

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Other_Age = 'other'
    Age_Choices = (
        (Adult,'Adult'),
        (Juvenile,'Juvenile'),
        (Other_Age,'Unknown'),
    )
    Age = models.CharField(
        max_length=10,
        choices=Age_Choices,
        default=Other_Age,
    )

    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    Other_Color = 'other'
    Fur_Choices = (
        (Gray,'Gray'),
        (Cinnamon,'Cinnamon'),
        (Black,'Black'),
        (Other_Color,'Unknown'),
    )
    Primary_Fur_Color = models.CharField(
        max_length=20,
        choices=Fur_Choices,
        default=Other_Color,
    )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    Other_Location = ''
    Location_Choices = (
        (Ground_Plane,'Ground Plane'),
        (Above_Ground,'Above Ground'),
        (Other_Location,'Unknown'),
    )
    Location = models.CharField(
        max_length=30,   
        choices=Location_Choices,
        default=Other_Location,
    )

    Specific_Location = models.TextField(max_length=200)
    Running = models.BooleanField(default=False,)
    Chasing = models.BooleanField(default=False,)
    Climbing = models.BooleanField(default=False,)
    Eating = models.BooleanField(default=False,)
    Foraging = models.BooleanField()
    Other_Activities = models.TextField(max_length=200)
    Kuks = models.BooleanField(default=False,)
    Quaas = models.BooleanField(default=False,)
    Moans = models.BooleanField(default=False,)
    Tail_flags = models.BooleanField(default=False,)
    Tail_twitches = models.BooleanField(default=False,)
    Approaches = models.BooleanField(default=False,)
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()

    def __str__(self):
        return self.Unique_Squirrel_ID

# Create your models here.
