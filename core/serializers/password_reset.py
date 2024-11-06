from rest_framework.serializers import Serializer, EmailField, CharField

class PasswordResetRequestSerializer(Serializer):
    email = EmailField()

class PasswordResetConfirmSerializer(Serializer):
    email = EmailField()
    token = CharField()
    new_password = CharField(min_length=8)
