from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Referral
from api.serializers import ReferralSerializer


@api_view(['GET', 'POST'])
def referral_list(request, format=None):
    """
    List all referrals, or create a new referral.
    """
    if request.method == 'GET':
        referrals = Referral.objects.all()
        serializer = ReferralSerializer(referrals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReferralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def referral_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        referral = Referral.objects.get(pk=pk)
    except Referral.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReferralSerializer(referral)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReferralSerializer(referral, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        referral.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
