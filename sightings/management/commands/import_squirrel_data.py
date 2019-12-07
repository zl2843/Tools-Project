import csv
from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
from distutils.util import strtobool

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('csv_file')


    def handle(self,*arg,**options):
        import csv
        import datetime
        path=options['csv_file']
        with open(path) as f:
            reader = csv.DictReader(f)
            data = list(reader)
            
            for line in data:

                sighting= Squirrel(
                        latitude=line['Y'],
                        longitude=line['X'],
                        squirrel_id=line['Unique Squirrel ID'],
                        shift=line['Shift'],
                        date=line['Date'],
                        age=line['Age'],
                        fur_color=line['Primary Fur Color'],
                        location=line['Location'],
                        specific_location=line['Specific Location'],
                        running=strtobool(line['Running']),
                        chasing=strtobool(line['Chasing']),
                        climbing=strtobool(line['Climbing']),
                        eating=strtobool(line['Eating']),
                        foraging=strtobool(line['Foraging']),
                        other_activities=line['Other Activities'],
                        kuks=strtobool(line['Kuks']),
                        quaas=strtobool(line['Quaas']),
                        moans=strtobool(line['Moans']), 
                        tail_flags=strtobool(line['Tail flags']),
                        tail_twitches=strtobool(line['Tail twitches']),
                        approaches=strtobool(line['Approaches']),
                        indifferent=strtobool(line['Indifferent']),
                        runs_from=strtobool(line['Runs from']),)

                sighting.save()
