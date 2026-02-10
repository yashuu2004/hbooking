from django.core.management.base import BaseCommand
from trips.models import State, City

DATA = {
    "Telangana": ["Hyderabad", "Warangal", "Karimnagar"],
    "Karnataka": ["Bangalore", "Mysore"],
    "Tamil Nadu": ["Chennai", "Coimbatore"],
    "Maharashtra": ["Mumbai", "Pune"],
    "Delhi": ["New Delhi"],
}

class Command(BaseCommand):
    help = "Load Indian states and cities"

    def handle(self, *args, **kwargs):
        for state_name, cities in DATA.items():
            state, _ = State.objects.get_or_create(name=state_name)
            for city in cities:
                City.objects.get_or_create(name=city, state=state)

        self.stdout.write(self.style.SUCCESS("States and Cities loaded"))
