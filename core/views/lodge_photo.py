from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from core.models import LodgePhoto
from core.serializers import LodgePhotoSerializer

class LodgePhotoViewSet(ModelViewSet):
    queryset = LodgePhoto.objects.all()
    serializer_class = LodgePhotoSerializer

    @action(detail=False, methods=["get"], permission_classes=[AllowAny()])
    def with_logo(self, request):
        photos = self.get_queryset()
        logo = photos.filter(photo__description="logo").first()
        
        photos_data = self.get_serializer(photos, many=True).data
        logo_data = self.get_serializer(logo).data if logo else None
        
        return Response({"photos": photos_data, "logo": logo_data})
