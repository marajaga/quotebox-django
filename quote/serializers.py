from rest_framework import serializers
from .models import Quote



class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'contributor']

    
    def create(self, validated_data):
        return Quote.objects.create(**validated_data)
