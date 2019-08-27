import uuid
from django.db import models
from .base import BaseModel

class Plant(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "plant"
        verbose_name_plural = "plants"

    def __str__(self):
        return self.name
