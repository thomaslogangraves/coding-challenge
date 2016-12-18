from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Referral

class ReferralSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Referral
        fields = ('url', 'id', 'title', 'clicks')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username')
