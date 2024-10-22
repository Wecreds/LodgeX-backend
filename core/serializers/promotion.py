from rest_framework.serializers import ModelSerializer

from core.models import Promotion

class PromotionSerializer(ModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"