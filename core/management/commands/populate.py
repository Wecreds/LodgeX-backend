from django.core.management.base import BaseCommand
from core.models import Category, Room

from core.management.resources import categories, rooms

class Command(BaseCommand):
    help = 'Populates the database.'

    def handle(self, *args, **kwargs):
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING('Categories already exist in the database.'))
        else:
            category_instances = [Category(**cat) for cat in categories]
            Category.objects.bulk_create(category_instances)
            self.stdout.write(self.style.SUCCESS('Categories populated successfully.'))
        
        if Room.objects.exists():
            self.stdout.write(self.style.WARNING('Rooms already exist in the database.'))
        else:
            room_instances = []
            for room in rooms:
                    category_instance = Category.objects.get(id=room["category"])
                    room_instance = Room(
                        name=room["name"],
                        single_beds=room["single_beds"],
                        couple_beds=room["couple_beds"],
                        price_by_day=room["price_by_day"],
                        description=room["description"],
                        category=category_instance
                    )
                    room_instances.append(room_instance)

            Room.objects.bulk_create(room_instances)
            self.stdout.write(self.style.SUCCESS('Rooms populated successfully.'))
        

        self.stdout.write('Successfully populated the database.')
