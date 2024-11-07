from django.core.management.base import BaseCommand
from core.models import Category, Room, Service, DiscountCoupon, User, Booking, BookingService, Cancellation, BookingRoom, RoomAvailability, Payment, Lodge, LodgeAmenity, LodgePaymentMethod, LodgePolicy
from uploader.models import Image
from django.contrib.auth.models import Group, Permission

from core.management.resources import categories, rooms, services, discount_coupons, groups, users, bookings, booking_services, cancellations, booking_rooms, rooms_availability, payments, images, lodges, lodgeAmendities, lodgePoliticies, lodgePaymentsMethods

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
                    booking_status=booking.get("booking_status", 1)
                )
                discount_coupon_id = booking.get("discount_coupon")
                if discount_coupon_id:
                    discount_coupon_instance = DiscountCoupon.objects.get(id=booking["discount_coupon"])
                    booking_instance.discount_coupon = discount_coupon_instance
                booking_instances.append(booking_instance)

            Booking.objects.bulk_create(booking_instances)
            self.stdout.write(self.style.SUCCESS('Bookings populated successfully.'))
        
        # Populates the booking services.
        if BookingService.objects.exists():
            self.stdout.write(self.style.WARNING('Booking Services already exist in the database.'))
        else:
            booking_service_instances = []
            for booking_service in booking_services:
                service_instance = Service.objects.get(id=booking_service["service"])
                booking_instance = Booking.objects.get(id=booking_service["booking"])
                booking_service_instance = BookingService(
                    service=service_instance,
                    booking=booking_instance
                )
                booking_service_instances.append(booking_service_instance)

            BookingService.objects.bulk_create(booking_service_instances)
            self.stdout.write(self.style.SUCCESS('Booking Services populated successfully.'))
        
        # Populates the cancellations.
        if Cancellation.objects.exists():
            self.stdout.write(self.style.WARNING('Cancellations already exist in the database.'))
        else:
            cancellation_instances = []
            for cancellation in cancellations:
                booking_instance = Booking.objects.get(id=cancellation["booking"])
                cancellation_instance = Cancellation(
                    reason=cancellation["reason"],
                    booking=booking_instance
                )
                cancellation_instances.append(cancellation_instance)

            Cancellation.objects.bulk_create(cancellation_instances)
            self.stdout.write(self.style.SUCCESS('Cancellations populated successfully.'))
        
        # Populates the booking rooms.
        if BookingRoom.objects.exists():
            self.stdout.write(self.style.WARNING('Booking Rooms already exist in the database.'))
        else:
            booking_room_instances = []
            for booking_room in booking_rooms:
                room_instance = Room.objects.get(id=booking_room["room"])
                booking_instance = Booking.objects.get(id=booking_room["booking"])
                booking_room_instance = BookingRoom(
                    room=room_instance,
                    booking=booking_instance
                )
                booking_room_instances.append(booking_room_instance)

            BookingRoom.objects.bulk_create(booking_room_instances)
            self.stdout.write(self.style.SUCCESS('Booking Rooms populated successfully.'))
        
        # Populates the rooms availability.
        if RoomAvailability.objects.exists():
            self.stdout.write(self.style.WARNING('Rooms Availability already exist in the database.'))
        else:
            room_availability_instances = []
            for room_availability in rooms_availability:
                room_instance = Room.objects.get(id=room_availability["room"])
                booking_instance = Booking.objects.get(id=room_availability["booking"])
                room_availability_instance = RoomAvailability(
                    start_date=room_availability["start_date"],
                    end_date=room_availability["end_date"],
                    room_status=room_availability["room_status"],
                    reason=room_availability.get("reason", None),
                    booking=booking_instance,
                    room=room_instance
                )
                room_availability_instances.append(room_availability_instance)

            RoomAvailability.objects.bulk_create(room_availability_instances)
            self.stdout.write(self.style.SUCCESS('Rooms Availability populated successfully.'))
        
        # Populates the payments.
        if Payment.objects.exists():
            self.stdout.write(self.style.WARNING('Payments already exist in the database.'))
        else:
            for payment in payments:
                booking_instance = Booking.objects.get(id=payment["booking"])
                # Since the bulk_create doesnt activate the save method, we need to create the models one by one.
                Payment.objects.create(
                    booking=booking_instance,
                    payment_status=payment["payment_status"]
                )

            self.stdout.write(self.style.SUCCESS('Payments populated successfully.'))


        if Image.objects.exists():
            self.stdout.write(self.style.WARNING('Images already exist in the database.'))
        else:
            images_instances = [Image(**img) for img in images]
            Image.objects.bulk_create(images_instances)
            self.stdout.write(self.style.SUCCESS('Images populated successfully.'))

        self.stdout.write('Successfully populated the database.')

        if Lodge.objects.exists():
            self.stdout.write(self.style.WARNING('Lodges already exist in the database.'))
        else:
            lodges_instances = [Lodge(**lodge) for lodge in lodges]
            Lodge.objects.bulk_create(lodges_instances)
            self.stdout.write(self.style.SUCCESS('Lodges populated successfully.'))
        
        if LodgeAmenity.objects.exists():
            self.stdout.write(self.style.WARNING('Lodge Amenities already exist in the database.'))
        else:
            lodge_amenities_instances = []
            for lodge_amenity in lodgeAmendities:
                lodge_instance = Lodge.objects.get(id=lodge_amenity["lodge"])
                lodge_amenity["lodge"] = lodge_instance
                lodge_amenity_instance = LodgeAmenity(**lodge_amenity)
                lodge_amenities_instances.append(lodge_amenity_instance)
            
            LodgeAmenity.objects.bulk_create(lodge_amenities_instances)
            self.stdout.write(self.style.SUCCESS('Lodge Amenities populated successfully.'))
        
        if LodgePolicy.objects.exists():
            self.stdout.write(self.style.WARNING('Lodge Policies already exist in the database.'))
        else:
            lodge_policies_instances = []
            for lodge_policy in lodgePoliticies:
                lodge_instance = Lodge.objects.get(id=lodge_policy["lodge"])
                lodge_policy["lodge"] = lodge_instance
                lodge_policy_instance = LodgePolicy(**lodge_policy)
                lodge_policies_instances.append(lodge_policy_instance)
            
            LodgePolicy.objects.bulk_create(lodge_policies_instances)
            self.stdout.write(self.style.SUCCESS('Lodge Policies populated successfully.'))

        if LodgePaymentMethod.objects.exists():
            self.stdout.write(self.style.WARNING('Lodge Payment Methods already exist in the database.'))
        else:
            lodge_payment_methods_instances = []
            for lodge_payment_method in lodgePaymentsMethods:
                lodge_instance = Lodge.objects.get(id=lodge_payment_method["lodge"])
                lodge_payment_method["lodge"] = lodge_instance
                lodge_payment_method_instance = LodgePaymentMethod(**lodge_payment_method)
                lodge_payment_methods_instances.append(lodge_payment_method_instance)
            
            LodgePaymentMethod.objects.bulk_create(lodge_payment_methods_instances)
            self.stdout.write(self.style.SUCCESS('Lodge Payment Methods populated successfully.'))
            
 