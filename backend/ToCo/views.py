from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProjectListCreateSerializer, MainContentSerializer, MainContentDeleteSerializer

from .models import MainContent

from rest_framework import viewsets
from rest_framework import status

from rest_framework.response import Response
from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated



# class ProjectCreateApiView(generics.CreateAPIView):
#     serializer_class = ProjectListCreateSerializer
#     parser_classes = [MultiPartParser, FormParser]
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(created_by=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ProjectListApiView(generics.ListAPIView):
#     queryset = MainContent.objects.all()
#     serializer_class = MainContentSerializer


# class BlogDeleteApiView(generics.DestroyAPIView):
#     queryset = MainContent.objects.all()
#     serializer_class = ProjectListCreateSerializer


class ContentListViewSet(viewsets.ModelViewSet):
    queryset = MainContent.objects.all()
    serializer_class = MainContentDeleteSerializer