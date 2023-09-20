from .models import Cheese
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# CheeseSerializer
class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model to serialize
        model = Cheese
        # The fields that should be included in the serialized output
        fields = ['id', 'name', 'origin_country', 'type']