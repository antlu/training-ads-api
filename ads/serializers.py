from rest_framework import serializers

from ads.models import Advertisement


class AdSerializer(serializers.ModelSerializer):
    """Ad model serializer."""

    class Meta(object):
        model = Advertisement
        fields = '__all__'
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
        request = self.context.get('request')
        if request is None:
            return
        if request.method == 'POST':
            return
        requested_fields = request.query_params.get('add')
        fields_to_exclude = (
            self.Meta.optional_fields if requested_fields is None
            else
            set(self.Meta.optional_fields) - set(requested_fields.split(','))
        )
        for field in fields_to_exclude:
            self.fields.pop(field)
