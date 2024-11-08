from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate

from core.serializers import BookingSerializer, UserSerializer
from core.models import User, Booking, Payment

from uploader.models import Document

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
   
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        restricted_fields = ["groups", "user_permissions", "is_staff", "is_superuser"]
        for field in restricted_fields:
            data.pop(field, None)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = User(**serializer.validated_data)
        user.set_password(serializer.validated_data['password'])

        documentInstance = Document.objects.get(id=data["document"])
        user.document = documentInstance
        user.save()

        group_name = "Customer"
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def verify_password(self, request):
        password = request.query_params.get("password")
        user = request.user

        if authenticate(email=user.email, password=password):
            return Response({"verified": True}, status=status.HTTP_200_OK)
        else:
            return Response({"verified": False}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def my_bookings(self, request):
        user = request.user
        my_bookings = Booking.objects.filter(user=user)

        if my_bookings.exists():
            bookings_with_payments = []
            
            for booking in my_bookings:
                payment = Payment.objects.filter(booking=booking).first()  
                booking_data = BookingSerializer(booking).data  
                
                if payment:
                    booking_data['payment_status'] = payment.get_payment_status_display()  
                    booking_data['payment_date'] = payment.payment_date 
                else:
                    booking_data['payment_status'] = 'No payment'
                    booking_data['payment_date'] = None

                bookings_with_payments.append(booking_data)
            
            return Response({"bookings": bookings_with_payments}, status=status.HTTP_200_OK)
        
        else:
            return Response({"bookings": []}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["patch"], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        user = request.user
        password = request.data.get("password")

        user.set_password(password)
        user.save()
        return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)

