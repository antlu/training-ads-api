from datetime import datetime

import pytz
from django.test import TestCase

from ads.models import Advertisement

TITLE = 'Coffee machine'
DESCRIPTION = 'Description of the item'
PRICE = 70000  # noqa: WPS432
PHOTO_LINK1 = 'http://link_to_photo1'
PHOTO_LINK2 = 'http://link_to_photo2'
PHOTO_LINK3 = 'http://link_to_photo3'
CREATED_AT = datetime(2020, 8, 26, tzinfo=pytz.UTC)  # noqa: WPS432


class AdTests(TestCase):
    """Tests."""

    @classmethod
    def setUpTestData(cls):
        """Add test data for all tests."""
        Advertisement.objects.create(
            title=TITLE,
            description=DESCRIPTION,
            price=PRICE,
            photo_link1=PHOTO_LINK1,
            photo_link2=PHOTO_LINK2,
            photo_link3=PHOTO_LINK3,
            created_at=CREATED_AT,
        )

    def test_ad_is_created(self):
        """Correct ad instance is created."""
        ad = Advertisement.objects.first()
        self.assertEqual(ad.title, TITLE)
        self.assertEqual(ad.description, DESCRIPTION)
        self.assertEqual(ad.price, PRICE)
        self.assertEqual(ad.photo_link1, PHOTO_LINK1)
        self.assertEqual(ad.photo_link2, PHOTO_LINK2)
        self.assertEqual(ad.photo_link3, PHOTO_LINK3)
        self.assertEqual(ad.created_at, CREATED_AT)
