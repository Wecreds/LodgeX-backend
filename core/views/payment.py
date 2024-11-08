from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from core.models import Payment, Booking
from core.serializers import PaymentSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def get_or_create_payment(self, request):
        booking_id = request.query_params.get("booking_id")
        
        if not booking_id:
            return Response({"detail": "booking_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response({"detail": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)
        
        payment = Payment.objects.filter(booking=booking).first()

        if payment:
            return Response(PaymentSerializer(payment).data, status=status.HTTP_200_OK)
        else:
            new_payment = Payment.objects.create(booking=booking)
            
            new_payment.payment_status = Payment.PaymentStatus.PENDING
            new_payment.save()

            return Response(PaymentSerializer(new_payment).data, status=status.HTTP_201_CREATED)
