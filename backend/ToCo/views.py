from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import MainContent
from .serializers import MainContentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET'])
# def get_blog(request):
#     Content = MainContent.objects.all()
#     serializer = MainContentSerializer(Content)
#     return Response(serializer.data)

class ContentListViewSet(ModelViewSet):
    queryset = MainContent
    serializer_class = MainContentSerializer
    parser_classes = [MultiPartParser, FormParser]


class ProjectCreateApiView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = MainContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)