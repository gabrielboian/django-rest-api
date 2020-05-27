from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalList
        fields = ['id', 'title', 'description', 'age', 'breed', 'state', 'city', 'size', 'date_rescue', 'gender', 'created_at', 'mode']