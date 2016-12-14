from django.db import models

class Referral(models.Model):
    title = models.CharField(max_length=30, unique=True)
    clicks = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='referrals', on_delete=models.CASCADE)
