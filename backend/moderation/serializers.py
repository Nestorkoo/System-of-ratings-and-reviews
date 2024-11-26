from rest_framework import serializers
from moderation.models import Reports
from tasks.models import Review
from django.shortcuts import get_object_or_404

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

class CreateReportSerializator(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['reason']

    def create(self, validated_data):
        user = self.context['request'].user
        review_id = self.context.get('review_id')

        if not review_id:
            raise serializers.ValidationError({'review_id': 'Review ID is required.'})

        review_obj = get_object_or_404(Review, id=review_id)

        report = Reports.objects.create(
            reported_by=user,
            review=review_obj,
            reason=validated_data['reason']
        )
        return report
    
class DeleteReviewSerializator(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Review
        fields = ['id']

    def validated_id(self, value):
        if not Review.objects.filter(id=value).exists():
            raise serializers.ValidationError('Review with this ID does not exist.')
        return value