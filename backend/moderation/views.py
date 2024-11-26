from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from config.permission import IsAdminOrModerator
from moderation.serializers import ReportSerializer, CreateReportSerializator, DeleteReviewSerializator
from moderation.models import Reports
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ReportListView(generics.ListAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsAdminOrModerator]
    
    def get(self, request, *args, **kwargs):
        reports = self.get_queryset()
        serializer = self.get_serializer(reports, many=True)
        
        return Response({
            "message": "List of all reports",
            "data": serializer.data
        })
    
class CreateReportView(generics.CreateAPIView):
    queryset = Reports.objects.all()
    serializer_class = CreateReportSerializator
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['review_id'] = self.kwargs.get('review_id')
        return context

    def perform_create(self, serializer):
        serializer.save()

class DeleteReviewView(generics.DestroyAPIView):
    serializer_class = DeleteReviewSerializator
    permission_classes = [IsAuthenticated, IsAdminOrModerator]

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            review_id = validated_data['id']
            
            from .models import Review
            review = get_object_or_404(Review, id=review_id)
            review.delete()

            return Response(
                {"message": f"Review with ID {review_id} has been deleted."}, 
                status=status.HTTP_200_OK
            )
            