import factory
from backend.models import Plant, Datapoint

class PlantFactory(factory.Factory):
    class Meta:
        model = Plant
    name = factory.Faker('company', locale='de_DE')

class DatapointFactory(factory.Factory):
    class Meta:
        model = Datapoint
    
    plant = factory.SubFactory(PlantFactory)