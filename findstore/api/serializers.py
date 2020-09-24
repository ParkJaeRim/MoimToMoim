from .models import Store, Reviews, TestReviews, Recommand
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class TestReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReviews
        fields = '__all__'


class RecommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommand
        fields = '__all__'