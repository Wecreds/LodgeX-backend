from rest_framework.serializers import ModelSerializer
from core.models import Lodge, LodgeAmenity, LodgePolicy, LodgePaymentMethod, LodgePhoto

class LodgeAmenitySerializer(ModelSerializer):
    class Meta:
        model = LodgeAmenity
        fields = ['id', 'name', 'icon']

class LodgePolicySerializer(ModelSerializer):
    class Meta:
        model = LodgePolicy
        fields = ['id', 'title', 'description', 'icon']

class LodgePaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = LodgePaymentMethod
        fields = ['id', 'method', 'icon']

class LodgeSerializer(ModelSerializer):
    amenities = LodgeAmenitySerializer(many=True, read_only=True)
    policies = LodgePolicySerializer(many=True, read_only=True)
    payment_methods = LodgePaymentMethodSerializer(many=True, read_only=True)

    class Meta:
        model = Lodge
        fields = [
            'id', 'lodge_name', 'lodge_location', 'lodge_description', 'lodge_landlord', 
            'amenities', 'policies', 'payment_methods'
        ]

class LodgePhotoSerializer(ModelSerializer):
    class Meta:
        model = LodgePhoto
        fields = "__all__"
        depth = 1