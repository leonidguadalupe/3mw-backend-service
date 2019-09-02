import decimal

from rest_framework import serializers
from backend.models import Datapoint as DatapointModel

class ReportSerializer(serializers.BaseSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(ReportSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        fields = ['id', 'datetime_generated__date',
                    'total_energy_expected', 'total_energy_observed', 
                    'total_irradiation_expected', 'total_irradiation_observed']

    def to_representation(self, instance):
        ret = instance
        ret['datetime_generated__date'] = ret['datetime_generated__date'].isoformat()[0:10]
        ret['total_energy_expected'] = round(decimal.Decimal(str(ret['total_energy_expected'])),3)
        ret['total_energy_observed'] = round(decimal.Decimal(str(ret['total_energy_observed'])),3)
        ret['total_irradiation_expected'] = round(decimal.Decimal(str(ret['total_irradiation_expected'])),3)
        ret['total_irradiation_observed'] = round(decimal.Decimal(str(ret['total_irradiation_observed'])),3)
        return ret