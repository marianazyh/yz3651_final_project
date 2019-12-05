import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Export the data in CSV fromat'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self,*args,**options):
        
