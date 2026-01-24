from django.db import models


class CustomModel(models.Model):
    def get_absolute_url(self) -> str:
        raise NotImplementedError

    class Meta:
        abstract = True
