from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer
from rest_framework.views import APIView
from users.models import CustomUser
from tasks.models import Review
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(f'Account {user} created', status=status.HTTP_201_CREATED)
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        username = self.kwargs.get('username')
        queryset = self.queryset

        if username:
            queryset = queryset.filter(username=username)
            if queryset:
                serializer = self.get_serializer (queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No profile found", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Please enter the username of the user', status=status.HTTP_400_BAD_REQUEST)