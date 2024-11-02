from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            else:
                raise serializers.ValidationError("Invalid username or password")
        else:
            raise serializers.ValidationError("Must include both username and password")