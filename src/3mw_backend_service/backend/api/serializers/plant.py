from rest_framework import serializers
from backend.models import Plant as PlantModel

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantModel
        fields = ['uid','name']