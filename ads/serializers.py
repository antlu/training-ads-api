from rest_framework import serializers

from ads.models import Advertisement


class AdSerializer(serializers.ModelSerializer):
    """Ad model serializer."""

    class Meta(object):
        model = Advertisement
        fields = ('title', 'price', 'photo_link1')
