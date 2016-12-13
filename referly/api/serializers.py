from rest_framework import serializers

from api.models import Referral

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('title', 'clicks')
