from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Referral

class ReferralSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Referral
        fields = ('url', 'id', 'title', 'clicks', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    referrals = serializers.PrimaryKeyRelatedField(many=True, queryset=Referral.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'referrals')
