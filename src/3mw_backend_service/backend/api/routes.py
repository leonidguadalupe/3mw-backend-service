from rest_framework import routers
from .views import PlantViewSet, DatapointViewSet

router = routers.DefaultRouter()
router.register(r'plants', PlantViewSet)
router.register(r'datapoints', DatapointViewSet)