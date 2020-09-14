from drf_yasg import openapi

info = openapi.Info(  # noqa: WPS110
    title="Ads API",
    default_version="v1",
)

add_param = openapi.Parameter(
    'add',
    openapi.IN_QUERY,
    description="A comma-delimited set of optional fields.",
    type=openapi.TYPE_STRING,
)

response_created = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={'id': openapi.Schema('ID', type=openapi.TYPE_INTEGER)},
)
