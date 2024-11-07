from rest_framework.serializers import ModelSerializer

from core.models import LodgePhoto

class LodgePhotoSerializer(ModelSerializer):
    class Meta:
        model = LodgePhoto
        fields = "__all__"
        depth = 1