from rest_framework import serializers

from ads.models import Advertisement


class AdSerializer(serializers.ModelSerializer):
    """Ad model serializer."""

    class Meta(object):
        model = Advertisement
        fields = ['title', 'price', 'photo_link1']
        required_fields = tuple(fields)
        optional_fields = (
            'photo_link2',
            'photo_link3',
            'description',
            'id',
            'created_at',
        )
        read_only_fields = ('created_at',)

    def __init__(self, *args, **kwargs):
        """
        Manage fields dynamically.

        On GET, add fields from the query string by the key `add`.
        On POST, use all fields.
        """  # noqa: DAR101
        super().__init__(*args, **kwargs)
        request = self.context['request']
        if request.method == 'POST':
            self.Meta.fields.extend(self.Meta.optional_fields)
            return
        self.Meta.fields = list(self.Meta.required_fields)
        requested_fields = request.query_params.get('add')
        if requested_fields is None:
            return
        for field in requested_fields.split(','):
            if field in self.Meta.optional_fields:
                self.Meta.fields.append(field)
