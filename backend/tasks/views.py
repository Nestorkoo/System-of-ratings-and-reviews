from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import *
from rest_framework import status
from rest_framework.views import APIView
from tasks.models import Review
from tasks.serializers import ReviewCreateSerializator, ReviewViewSerializator
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializator

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewViewList(generics.ListAPIView):
    serializer_class = ReviewViewSerializator
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        return Review.objects.filter(user=user)

class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewViewSerializator
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        user = self.request.user

        if review.user != user:
            raise PermissionDenied('You do not have permission to delete this review')
        
        review.delete()
        
        return Response(f'{review} deleted successful', status=status.HTTP_200_OK)

class StatisticReviewView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewViewSerializator

    def get(self, request, *args, **kwargs):
        company_name = self.kwargs.get('company')
        queryset = self.queryset
        
        if company_name:
            queryset = queryset.filter(manufacturer_company=company_name)
        
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            "message": f'Reviews with company name {company_name}:',
            'reviews': serializer.data
        }
        )

        