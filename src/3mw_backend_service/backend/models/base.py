from django.db import models

class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        abstract=True