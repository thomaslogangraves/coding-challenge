from rest_framework import serializer_class

from referrals.models import referrals

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('title', 'clicks')
