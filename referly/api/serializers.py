from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Referral

class ReferralSerializer(serializers.ModelSerializer):
    ambassador = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Referral
        fields = ('id', 'title', 'clicks', 'ambassador')

class UserSerializer(serializers.ModelSerializer):
    referrals = serializers.PrimaryKeyRelatedField(many=True, queryset=Referral.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'referrals')
