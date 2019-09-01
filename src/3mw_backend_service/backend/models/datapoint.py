from django.db import models

from .base import BaseModel

class Datapoint(BaseModel):
    plant = models.ForeignKey("Plant", verbose_name="plant_id", on_delete=models.CASCADE)
    datetime_generated = models.DateTimeField()
    energy_expected = models.DecimalField(max_digits=40, decimal_places=14)
    energy_observed = models.DecimalField(max_digits=40, decimal_places=14)
    irradiation_expected = models.DecimalField(max_digits=40, decimal_places=14)
    irradiation_observed = models.DecimalField(max_digits=40, decimal_places=14)

    class Meta:
        unique_together = ('plant','datetime_generated')
        indexes = [
            models.Index(fields=['plant','datetime_generated'])
        ]
        verbose_name = "datapoint"
        verbose_name_plural = "datapoints"

    def __str__(self):
        return self.plant.name