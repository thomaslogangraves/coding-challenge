from api.models import Referral
from api.serializers import ReferralSerializer
from rest_framework import generics


class ReferralList(generics.ListCreateAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


class ReferralDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
