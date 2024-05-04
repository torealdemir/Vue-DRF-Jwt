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

class ContentListViewSet(viewsets.ModelViewSet):
    queryset = MainContent.objects.all()
    serializer_class = ProjectListCreateSerializer