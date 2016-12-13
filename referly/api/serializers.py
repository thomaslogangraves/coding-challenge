from rest_framework import serializer_class

from api.models import Referral

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('title', 'clicks')
