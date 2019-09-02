import json
import requests

from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Datapoint as DatapointModel, Plant as PlantModel
from backend.utils import bulk_upsert_datapoints
from backend.api.serializers import DatapointSerializer


class DatapointViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = DatapointModel.objects.all()
    serializer_class = DatapointSerializer

 
class FetchMonitoringViewSet(APIView):
    def get(self, request, format=None) -> Response:
        plant_id = request.GET.get("plant-id")
        from_ = request.GET.get("from")
        to_ = request.GET.get("to")
        try:
            r = requests.get('http://192.168.2.18:5000/', 
                params= {
                    'plant-id': plant_id,
                    'from':from_,
                    'to':to_
                },
                timeout= 5
        )
        except requests.exceptions.RequestException as e: 
            print(e)
        
        result = r.json()
        
        def unpack(n):
            return DatapointModel(
                plant=PlantModel.objects.get(uid=plant_id),
                datetime_generated=n["datetime"],
                energy_expected=n["expected"]["energy"],
                energy_observed=n["observed"]["energy"],
                irradiation_expected=n["expected"]["irradiation"],
                irradiation_observed=n["observed"]["irradiation"]
            )
        unpacked_list = list(map(unpack,result["data"]))
        bulk_upsert_datapoints(unpacked_list)
        return Response({"data": result})