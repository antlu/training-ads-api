from datetime import datetime

import pytz
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ads.factories import AdFactory
from ads.models import Advertisement
from ads.serializers import AdSerializer


class AdModelTests(TestCase):
    """Tests for the Advertisement model."""

    def test_ad_is_created(self):  # noqa: WPS210
        """A correct ad instance is created."""
        TITLE = 'Coffee machine'
        DESCRIPTION = 'Description of the item'
        PRICE = 70000  # noqa: WPS432
        PHOTO_LINK1 = 'http://link-to-photo1.example.com'
        PHOTO_LINK2 = 'http://link-to-photo2.example.com'
        PHOTO_LINK3 = 'http://link-to-photo3.example.com'
        CREATED_AT = datetime(2020, 8, 26, tzinfo=pytz.UTC)  # noqa: WPS432

        ad = Advertisement.objects.create(
            title=TITLE,
            description=DESCRIPTION,
            price=PRICE,
            photo_link1=PHOTO_LINK1,
            photo_link2=PHOTO_LINK2,
            photo_link3=PHOTO_LINK3,
            created_at=CREATED_AT,
        )
        self.assertEqual(str(ad), TITLE)
        self.assertEqual(ad.title, TITLE)
        self.assertEqual(ad.description, DESCRIPTION)
        self.assertEqual(ad.price, PRICE)
        self.assertEqual(ad.photo_link1, PHOTO_LINK1)
        self.assertEqual(ad.photo_link2, PHOTO_LINK2)
        self.assertEqual(ad.photo_link3, PHOTO_LINK3)
        self.assertEqual(ad.created_at, CREATED_AT)


class AdsAPITests(APITestCase):
    """API tests."""

    def test_ad_creation(self):
        """New ad gets created and its ID is returned."""
        url = reverse('ad-list')
        ad = AdFactory.build()
        serializer = AdSerializer(ad)
        response = self.client.post(url, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        saved_ad = Advertisement.objects.first()
        self.assertEqual(saved_ad.title, ad.title)
        self.assertEqual(response.data['id'], saved_ad.id)

    def test_reading_a_paginated_list(self):
        """List data is readable and paginated."""
        url = reverse('ad-list')
        AdFactory.create_batch(20)  # noqa: WPS432
        response = self.client.get(url, {'page': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_reading_a_single_ad(self):
        """A single ad is readable."""
        ad = AdFactory()
        url = reverse('ad-details', args=[ad.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], ad.title)

    def test_required_and_optional_fields(self):
        """Required fields are always in response, optional may be omitted."""
        ad = AdFactory()
        url = reverse('ad-details', args=[ad.id])
        response_for_required_fields = self.client.get(url)
        self.assertTupleEqual(
            tuple(response_for_required_fields.data.keys()),
            ('title', 'price', 'photo_link1'),
        )
        response_for_optional_fields = self.client.get(
            url, {'add': 'description,created_at'},
        )
        self.assertTupleEqual(
            tuple(response_for_optional_fields.data.keys()),
            ('title', 'description', 'price', 'photo_link1', 'created_at'),
        )

    def test_sorting(self):
        """Results are sortable by price and time."""
        url = reverse('ad-list')
        AdFactory.create_batch(2)

        for field in ('price', '-price', 'created_at', '-created_at'):
            ordered_queryset = Advertisement.objects.order_by(field)
            response = self.client.get(url, {'add': 'id', 'ordering': field})
            self.assertEqual(
                response.data['results'][0]['id'], ordered_queryset.first().id,
            )
