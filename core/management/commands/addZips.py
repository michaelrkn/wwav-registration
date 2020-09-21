from core.models import Zip

from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    help = 'Adds Zip models'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Clearing current zips'))
        Zip.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared current zips'))
        self.stdout.write(self.style.SUCCESS('Starting Zip creation'))
        with open('zipState.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                z=Zip(zip=row[0],state=row[1],link=row[2],mail_only=row[3])
                z.save()



        self.stdout.write(self.style.SUCCESS('Finished Zip creation'))

