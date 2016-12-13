from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Referral
from api.serializers import ReferralSerializer


class ReferralList(APIView):
    """
    List all referrals, or create a new referral.
    """
    def get(self, request, format=None):
        referrals = Referral.objects.all()
        serializer = ReferralSerializer(referrals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReferralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReferralDetail(APIView):
    """
    Retrieve, update or delete a referral instance.
    """
    def get_object(self, pk):
        try:
            return Referral.objects.get(pk=pk)
        except Referral.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        referral = self.get_object(pk)
        serializer = ReferralSerializer(referral)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        referral = self.get_object(pk)
        serializer = ReferralSerializer(referral, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        referral = self.get_object(pk)
        referral.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
