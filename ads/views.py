from rest_framework import filters, generics

from ads.models import Advertisement
from ads.serializers import AdSerializer


class AdList(generics.ListCreateAPIView):
    """A list view for ads."""

    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('price', 'created_at')
    ordering = '-created_at'


class AdDetails(generics.RetrieveAPIView):
    """A detail view for an ad."""

    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer
