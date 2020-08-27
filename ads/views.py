from rest_framework import generics

from ads.models import Advertisement
from ads.serializers import AdSerializer


class AdList(generics.ListAPIView):
    """A list view for ads."""

    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class AdDetails(generics.RetrieveAPIView):
    """A detail view for an ad."""

    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer
