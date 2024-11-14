from rest_framework import serializers
from tasks.models import Review

class ReviewCreateSerializator(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('username','content', 'manufacturer_company',  'image_url', 'rating')

    def create(self, validated_data):
        user = self.context['request'].user
        if 'content' not in validated_data:
            raise serializers.ValidationError('Please enter a short description about your review!')
        if validated_data['rating'] > 10:
            raise serializers.ValidationError('Please enter a number from 1 to 10!')
        review = Review(
            user=user,
            content=validated_data['content'],
            manufacturer_company=validated_data['manufacturer_company'],
            image_url=validated_data['image_url'],
            rating=validated_data['rating'],

        )
        
        review.save()
        return review
class ReviewViewSerializator(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=('username', 'content','manufacturer_company','image_url', 'rating', 'created_at')
    