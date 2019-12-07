from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import CSV'

    def add_arguments(self,path):
        path.add_argument('csv_file',nargs='+',type=str)

    def handle(self,*arg,**options):
        import csv
        import datetime
        path=str(options['csv_file'][0])
        with open(path) as f:
            data=csv.reader(f)
            next(data)
            counter=0
            
            for line in data:
                for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                    if line[i]=='false':
                        line[i]= False
                    else:
                        line[i]= True

                line[5]=datetime.datetime.strptime(line[5],"%m%d%Y").strftime("%Y-%m-%d")
                sighting= Squirrel(latitude=line[1],
                        longitude=line[0],
                        squirrel_id=line[2],
                        shift=line[4],
                        date=line[5],
                        age=line[7],
                        fur_color=line[8],
                        location=line[12],
                        specific_location=line[14],
                        running=line[15],
                        chasing=line[16],
                        climbing=line[17],
                        eating=line[18],
                        foraging=line[19],
                        other_activities=line[20],
                        kuks=line[21],
                        quaas=line[22],
                        moans=line[23], 
                        tail_flags=line[24],
                        tail_twitches=line[25],
                        approaches=line[26],
                        indifferent=line[27],
                        runs_from=line[28],)

                sighting.save()
