from rest_framework import serializers
from core.models import Lodge, LodgeAmenity, LodgePolicy, LodgePaymentMethod

class LodgeAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LodgeAmenity
        fields = ['id', 'name', 'icon']

class LodgePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = LodgePolicy
        fields = ['id', 'title', 'description', 'icon']

class LodgePaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = LodgePaymentMethod
        fields = ['id', 'method', 'icon']

class LodgeSerializer(serializers.ModelSerializer):
    amenities = LodgeAmenitySerializer(many=True, read_only=True)
    policies = LodgePolicySerializer(many=True, read_only=True)
    payment_methods = LodgePaymentMethodSerializer(many=True, read_only=True)

    class Meta:
        model = Lodge
        fields = [
            'id', 'lodge_name', 'lodge_location', 'lodge_description', 'lodge_landlord', 
            'amenities', 'policies', 'payment_methods'
        ]
