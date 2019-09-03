import json

from django.db.models import Sum, Count, Avg, Q
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Datapoint as DatapointModel, Plant as PlantModel
from backend.utils import bulk_upsert_datapoints
from backend.api.serializers import ReportSerializer

class ReportingViewSet(APIView):
    def get(self, request, format=None) -> Response:
        plant_id = request.GET.get("plant-id")
        date_ = request.GET.get("date")
        
        year, month = date_.split('-')

        metrics =  {
            'total_energy_observed': Sum('energy_observed'),
            'total_energy_expected': Sum('energy_expected'),
            'total_irradiation_expected': Sum('irradiation_expected'),
            'total_irradiation_observed': Sum('irradiation_observed'),
            # 'avg_charged_amount': Avg('charged_amount'),
            # 'unique_users': Count('user', distinct=True),
        }
        
        result = ReportSerializer(DatapointModel.objects.filter(
            datetime_generated__year=year,
            datetime_generated__month=month
            ).values('datetime_generated__date').annotate(**metrics), 
            many=True, context={'request': request}
        )
        
        return Response({"data": result.data})