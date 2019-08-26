from rest_framework import serializers
from backend.models import Datapoint as DatapointModel

class DatapointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatapointModel
        fields = ['id', 'plant', 'datetime_generated',
                    'energy_expected', 'energy_observed', 
                    'irradiation_expected', 'irradiation_observed']
