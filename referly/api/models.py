from django.db import models

class Referral(models.Model):
    title = models.CharField(max_length=30, unique=True)
    clicks = models.IntegerField(default=0)
