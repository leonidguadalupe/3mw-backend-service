from rest_framework import viewsets
from backend.models import Plant as PlantModel
from ..serializers import PlantSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = PlantModel.objects.all()
    serializer_class = PlantSerializer
