from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Feedback
from core.serializers import FeedbackSerializer

class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @action(detail=False, methods=["get"])
    def approved(self, request):
        queryset = Feedback.objects.filter(review_status=Feedback.FeedbackStatus.APPROVED)
        serializer = FeedbackSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def pending(self, request):
        queryset = Feedback.objects.filter(review_status=Feedback.FeedbackStatus.PENDING)
        serializer = FeedbackSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def declined(self, request):
        queryset = Feedback.objects.filter(review_status=Feedback.FeedbackStatus.DECLINED)
        serializer = FeedbackSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)