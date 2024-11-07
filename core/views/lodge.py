from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action

from uploader.models import Image

from core.models import Lodge, LodgeAmenity, LodgePolicy, LodgePaymentMethod, LodgePhoto
from core.serializers import (
    LodgeSerializer,
    LodgeAmenitySerializer,
    LodgePolicySerializer,
    LodgePaymentMethodSerializer,
    LodgePhotoSerializer
)

class LodgeViewSet(ModelViewSet):
    queryset = Lodge.objects.all()
    serializer_class = LodgeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  
        return [IsAuthenticated()]
    
class LodgeAmenityViewSet(ModelViewSet):
    queryset = LodgeAmenity.objects.all()
    serializer_class = LodgeAmenitySerializer

class LodgePolicyViewSet(ModelViewSet):
    queryset = LodgePolicy.objects.all()
    serializer_class = LodgePolicySerializer

class LodgePaymentMethodViewSet(ModelViewSet):
    queryset = LodgePaymentMethod.objects.all()
    serializer_class = LodgePaymentMethodSerializer

class LodgePhotoViewSet(ModelViewSet):
    queryset = LodgePhoto.objects.all()
    serializer_class = LodgePhotoSerializer

    @action(detail=False, methods=["get"], permission_classes=[AllowAny])
    def with_logo(self, request):
        photos = self.get_queryset()
        logo = photos.filter(photo__description="logo").first()
        
        photos_data = self.get_serializer(photos, many=True).data
        logo_data = self.get_serializer(logo).data if logo else None
        
        return Response({"photos": photos_data, "logo": logo_data})
