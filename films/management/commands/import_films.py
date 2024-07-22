import csv
import os
from django.core.management.base import BaseCommand, CommandError
from films.models import Film


class Command(BaseCommand):
    help = 'Import films from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        if not os.path.exists(csv_file):
            raise CommandError(f"File '{csv_file}' does not exist")

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                film, created = Film.objects.get_or_create(
                    name=row['name'],
                    director=row['director'],
                    year=row['year'],
                    genre=row['genre'],
                    synopsis=row['synopsis'],
                    poster=row['poster'],
                    video_link=row['video_link']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added film '{film.name}'"))
                else:
                    self.stdout.write(f"Film '{film.name}' already exists")

        self.stdout.write(self.style.SUCCESS("Import completed successfully"))
