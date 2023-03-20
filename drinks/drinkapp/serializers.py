# we use serializer when we want to return our model through api
from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.modelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
