from django.core.management.base import BaseCommand
from trips.models import State, City
import csv
import os

class Command(BaseCommand):
    help = "Load all Indian states and cities"

    def handle(self, *args, **kwargs):
        csv_file = os.path.join(os.path.dirname(__file__), "india_cities.csv")

        with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                state, _ = State.objects.get_or_create(name=row["state"])
                City.objects.get_or_create(
                    name=row["city"],
                    state=state
                )

        self.stdout.write(self.style.SUCCESS("All Indian states & cities loaded"))
