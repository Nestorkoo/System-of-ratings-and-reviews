from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'roles', 'password']

    def create(self, validated_data):
        if 'roles' not in validated_data:
            validated_data['roles'] = ['user']
        if len(validated_data['password']) < 6:
            raise serializers.ValidationError('the password should be at least 6 characters long')

        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
