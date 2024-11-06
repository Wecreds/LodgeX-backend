from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import User
from core.serializers import PasswordResetRequestSerializer

class PasswordResetRequestView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            try:
                user = User.objects.get(email=email)  
            except User.DoesNotExist:
                return Response({"detail": "No account found with the given email."}, status=status.HTTP_404_NOT_FOUND)

            token = default_token_generator.make_token(user)
            send_mail(
                'Password Reset Code',
                f'Your password reset code is: {token}',
                user.email, 
                [email],
                fail_silently=False,
            )
            return Response({"detail": "Password reset code sent by email."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
