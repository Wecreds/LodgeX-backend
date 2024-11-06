from rest_framework.serializers import ModelSerializer, ValidationError

from core.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1

    def update(self, instance, validated_data):
        current_user = self.context.get('request').user
            
        if instance != current_user:
            raise ValidationError("You can only alter your own user.")
            
        validated_data.pop('password', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        instance.save()
        return instance
