from django.core.management.base import BaseCommand
from trips.models import State, City
import csv
import os

class Command(BaseCommand):
    help = "Load Indian states and cities from CSV"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(
            os.path.dirname(__file__),
            "indian_states_cities.csv"
        )

        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR("CSV file not found"))
            return

        with open(csv_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                state_name = row["state"].strip()
                city_name = row["city"].strip()

                state, _ = State.objects.get_or_create(name=state_name)
                City.objects.get_or_create(name=city_name, state=state)

        self.stdout.write(self.style.SUCCESS("✅ All states and cities loaded"))
