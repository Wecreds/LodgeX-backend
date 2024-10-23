from rest_framework.viewsets import ModelViewSet

from core.models import Feedback
from core.serializers import FeedbackSerializer

class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer