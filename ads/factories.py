import factory
import pytz

from ads.models import Advertisement


class AdFactory(factory.django.DjangoModelFactory):
    """Ad builder."""

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    price = factory.Faker('random_int', max=100000)  # noqa: WPS432
    photo_link1 = factory.Faker('image_url')
    photo_link2 = factory.Faker('image_url')
    photo_link3 = factory.Faker('image_url')
    created_at = factory.Faker('date_time_this_decade', tzinfo=pytz.UTC)

    class Meta(object):
        model = Advertisement
