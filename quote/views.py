from django.shortcuts import render
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class QuoteViewSet(viewsets.ModelViewSet):
   

    def create(self,request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        queryset = Quote.objects.filter(published=True)
        print(queryset)
        quote = queryset.random()[0]
        print(quote)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)