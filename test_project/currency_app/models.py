from django.db import models


class Currency(models.Model):
    usd_to_rub = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
