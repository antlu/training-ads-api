class DynamicFieldsMixin(object):
    """A serializer mixin that lets using optional fields."""

    class Meta(object):
        optionial_fields = ()

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
