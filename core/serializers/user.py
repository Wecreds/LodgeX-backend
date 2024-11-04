from rest_framework.serializers import ModelSerializer

from core.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1

        def update(self, instance, validated_data):
            current_user = self.context.get('request').user
            
            if instance != current_user:
                raise serializers.ValidationError("You can only alter your own user.")
            
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            
            instance.save()
            return instance
