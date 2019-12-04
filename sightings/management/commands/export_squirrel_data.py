from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'Export a csv file'
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'w') as f:
            writer = csv.writer(f)
            header = ['latitude',
                    'longitude',
                    'squirrel_id',
                    'shift',
                    'date',
                    'age',
                    'fur_color',
                    'location',
                    'specific_location',
                    'running',
                    'chasing',
                    'climbing',
                    'eating',
                    'foraging',
                    'other_activities',
                    'kuks',
                    'quaas',
                    'moans',
                    'tail_flags',
                    'tail_twitches',
                    'approaches',
                    'indifferent',
                    'runs_from',]
            writer.writerow(header)

            for obj in Squirrel.objects.all():
                data = [obj.latitude,
                        obj.longitude,
                        obj.squirrel_id,
                        obj.shift,
                        obj.date,
                        obj.age,
                        obj.fur_color,
                        obj.location,
                        obj.specific_location,
                        obj.running,
                        obj.chasing,
                        obj.climbing,
                        obj.eating,
                        obj.foraging,
                        obj.other_activities,
                        obj.kuks,
                        obj.quaas,
                        obj.moans,
                        obj.tail_flags,
                        obj.tail_twitches,
                        obj.approaches,
                        obj.indifferent,
                        obj.runs_from,]
                writer.writerow(data)

