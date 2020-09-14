from rest_framework import serializers

from ads.mixins import DynamicFieldsMixin
from ads.models import Advertisement


class AdSerializer(serializers.ModelSerializer):
    """A static ad model serializer which always uses all the model fields."""

    class Meta(object):
        model = Advertisement
        fields = '__all__'
        read_only_fields = ('created_at',)


class DynamicAdSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    """A dynamic ad model serializer."""

    class Meta(DynamicFieldsMixin.Meta, AdSerializer.Meta):
        optional_fields = (
            'photo_link2',
            'photo_link3',
            'description',
            'id',
            'created_at',
        )
