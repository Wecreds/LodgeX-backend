from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate

from core.models import User
from core.serializers import UserSerializer

from uploader.models import Document

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
   
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        restricted_fields = ["groups", "user_permissions", "is_staff", "is_superuser"]
        for field in restricted_fields:
            data.pop(field, None)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = User(**serializer.validated_data)
        user.set_password(serializer.validated_data['password'])

        documentInstance = Document.objects.get(id=data["document"])
        user.document = documentInstance
        user.save()

        group_name = "Customer"
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


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
            return Response({"verified": False}, status=status.HTTP_200_OK)
