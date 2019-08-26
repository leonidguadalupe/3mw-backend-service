from rest_framework import viewsets
from backend.models import Datapoint as DatapointModel
from backend.api.serializers import DatapointSerializer

class DatapointViewSet(viewsets.ModelViewSet):
    queryset = DatapointModel.objects.all()
    serializer_class = DatapointSerializer
