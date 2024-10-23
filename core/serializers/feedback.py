from rest_framework.serializers import ModelSerializer

from core.models import Feedback

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"