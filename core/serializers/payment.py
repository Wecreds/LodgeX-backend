from rest_framework import serializers
from core.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    payment_status_display = serializers.CharField(source='get_payment_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id',
            'payment_status_display',   
            'booking_price',
            'service_price',
            'payment_date',
            'payment_method_display',    
            'booking',
        ]
        read_only_fields = ['id']
