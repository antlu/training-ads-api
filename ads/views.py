from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, generics, status
from rest_framework.response import Response

from ads.models import Advertisement
from ads.openapi import add_param, response_created
from ads.serializers import AdSerializer, DynamicAdSerializer

GET_REQUEST_NAME = 'get'


@method_decorator(
    swagger_auto_schema(
        request_body=AdSerializer,
        responses={status.HTTP_201_CREATED: response_created},
    ), name='post',
)
@method_decorator(
    swagger_auto_schema(manual_parameters=[add_param]), name=GET_REQUEST_NAME,
)
@method_decorator(cache_page(settings.CACHE_TTL), name=GET_REQUEST_NAME)
class AdList(generics.ListCreateAPIView):
    """A list view for adding and viewing ads."""

    queryset = Advertisement.objects.all()
    serializer_class = DynamicAdSerializer
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


@method_decorator(
    swagger_auto_schema(manual_parameters=[add_param]), name=GET_REQUEST_NAME,
)
@method_decorator(cache_page(settings.CACHE_TTL), name=GET_REQUEST_NAME)
class AdDetails(generics.RetrieveAPIView):
    """A detail view for viewing an ad."""

    queryset = Advertisement.objects.all()
    serializer_class = DynamicAdSerializer
