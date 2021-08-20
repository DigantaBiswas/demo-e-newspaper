# Create your models here.
from datetime import datetime, timezone

import django
from django.db import models

class BaseAbstractModel(models.Model):
    """
    This model is an abstract model
    This model contains basic fields for all other models.
    This model will be designed as a parent model for every other models
    """
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        abstract = True
        app_label = "base"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.now(tz=timezone.utc)
        self.updated_at = datetime.now(tz=timezone.utc)
        return super(BaseAbstractModel, self).save(*args, **kwargs)
