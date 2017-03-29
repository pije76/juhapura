from django.db import models
from juhapura.utils.models.ChoiceLists import status_list

class StatusField(models.Model):
    status_lkup = models.IntegerField(choices=status_list)
    status = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        abstract = True

