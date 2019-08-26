from rest_framework import serializers
from backend.models import Plant as PlantModel

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlantModel
        fields = ['uid', 'name']
