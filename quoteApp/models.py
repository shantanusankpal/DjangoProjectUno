from django.db import models


class Quote(models.Model):
    written_by = models.CharField(max_length=30)
    quote = models.CharField(max_length=256)
    value = models.IntegerField()


# Create your models here.mo
