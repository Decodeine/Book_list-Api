from rest_framework import serializers
from .models import Book, Review

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','author','price','publication_date']

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['reviewer', 'review', 'rating']
