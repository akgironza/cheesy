from django.shortcuts import render
from .models import Cheese
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CheeseSerializer

# Create your views here.

class CheeseViewSet(viewsets.ModelViewSet):
    # MAIN QUERY for the INDEX route
    queryset = Cheese.objects.all()
    # Serializer class for serializing output
    serializer_class = CheeseSerializer
    # Optional permission class set permission level
    permission_classes = [permissions.AllowAny]