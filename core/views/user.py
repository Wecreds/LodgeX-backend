from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate

from core.models import User
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def verify_password(self, request):
        password = request.query_params.get("password")
        user = request.user

        if authenticate(email=user.email, password=password):
            return Response({"verified": True}, status=status.HTTP_200_OK)
        else:
            return Response({"verified": False}, status=status.HTTP_400_BAD_REQUEST)
