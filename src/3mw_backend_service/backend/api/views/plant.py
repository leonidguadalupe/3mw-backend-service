from rest_framework import viewsets
from backend.models import Plant as PlantModel
from ..serializers import PlantSerializer
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

class PlantViewSet(viewsets.ModelViewSet):
    queryset = PlantModel.objects.all()
    serializer_class = PlantSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)