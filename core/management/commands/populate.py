from django.core.management.base import BaseCommand
from core.models import Category, Room, Service, DiscountCoupon, User, Booking
from django.contrib.auth.models import Group, Permission

from core.management.resources import categories, rooms, services, discount_coupons, groups, users, bookings

class Command(BaseCommand):
    help = 'Populates the database.'

    def handle(self, *args, **kwargs):
        # Populates the categories.
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING('Categories already exist in the database.'))
        else:
            category_instances = [Category(**cat) for cat in categories]
            Category.objects.bulk_create(category_instances)
            self.stdout.write(self.style.SUCCESS('Categories populated successfully.'))
        
        # Populates the rooms.
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
        
        # Populates the services.
        if Service.objects.exists():
            self.stdout.write(self.style.WARNING('Services already exist in the database.'))
        else:
            service_instances = [Service(**service) for service in services]
            Service.objects.bulk_create(service_instances)
            self.stdout.write(self.style.SUCCESS('Services populated successfully.'))

        if DiscountCoupon.objects.exists():
            self.stdout.write(self.style.WARNING('Discount Coupons already exist in the database.'))
        else:
            discount_coupon_instances = [DiscountCoupon(**discount_coupon) for discount_coupon in discount_coupons]
            DiscountCoupon.objects.bulk_create(discount_coupon_instances)
            self.stdout.write(self.style.SUCCESS('Discount Coupons populated successfully.'))    
        
       # Populates the groups and assigns permissions.
        if Group.objects.exists():
            self.stdout.write(self.style.WARNING('Groups already exist in the database.'))
        else:
            for group_name, permissions in groups.items():
                group = Group.objects.create(name=group_name)
                self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" created successfully.'))

                permission_objects = Permission.objects.filter(codename__in=permissions)
                group.permissions.set(permission_objects)
                group.save()
                self.stdout.write(self.style.SUCCESS(f'Permissions assigned to group "{group_name}".'))

        # Populates the users.
        if User.objects.exists():
            self.stdout.write(self.style.WARNING('Users already exist in the database.'))
        else:
            for user in users:
                user_instance = User(
                    name=user["name"],
                    email=user["email"],
                    telephone=user["telephone"],
                    personal_info=user["personal_info"],
                    is_staff=user.get("is_staff", False),
                    is_superuser=user.get("is_superuser", False)
                )
                user_instance.set_password(user["password"])
                user_instance.save()  

                group_instance = Group.objects.get(name=user["group"])
                user_instance.groups.set([group_instance])

                self.stdout.write(self.style.SUCCESS(f'User "{user["name"]}" created and assigned to group "{user["group"]}".'))

        # Populates the bookings.
        if Booking.objects.exists():
            self.stdout.write(self.style.WARNING('Bookings already exist in the database.'))
        else:
            booking_instances = []
            for booking in bookings:
                user_instance = User.objects.get(id=booking["user"])
                booking_instance = Booking(
                    user=user_instance,
                )
                discount_coupon_id = booking.get("discount_coupon")
                if discount_coupon_id:
                    discount_coupon_instance = DiscountCoupon.objects.get(id=booking["discount_coupon"])
                    booking_instance.discount_coupon = discount_coupon_instance
                booking_instances.append(booking_instance)

            Booking.objects.bulk_create(booking_instances)
            self.stdout.write(self.style.SUCCESS('Bookings populated successfully.'))

        self.stdout.write('Successfully populated the database.')
