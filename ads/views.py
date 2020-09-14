from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import filters, generics
from rest_framework.response import Response

from ads.models import Advertisement
from ads.serializers import AdSerializer


@method_decorator(cache_page(settings.CACHE_TTL), name='get')
class AdList(generics.ListCreateAPIView):
    """A list view for adding and viewing ads."""

    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('price', 'created_at')
    ordering = '-created_at'

    def post(self, *args, **kwargs):
        """Return a customized response with the id of the ad."""  # noqa: DAR101,E501
        response = super().post(*args, **kwargs)
        return Response(
            {'id': response.data['id']},
            status=response.status_code,
        )


@method_decorator(cache_page(settings.CACHE_TTL), name='get')
class AdDetails(generics.RetrieveAPIView):
    """A detail view for viewing an ad."""

    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer
