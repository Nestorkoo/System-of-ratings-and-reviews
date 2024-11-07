from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from tasks.models import Review
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def create(self, validated_data):
        
        if len(validated_data['password']) < 6:
            raise serializers.ValidationError('the password should be at least 6 characters long')
        
        if 'email' not in validated_data:
            raise serializers.ValidationError('Please enter your email!')
        
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            role='user',
        )
        
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


class UserProfileSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'reviews')

    def get_reviews(self, obj):
        return obj.reviews.values('id', 'content', 'rating', 'created_at')


