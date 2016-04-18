"""Tests for the views of the ``hero_slider`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin

from ..views import GetCTypeDetails


class GetCTypeDetailsTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``GetCTypeDetails`` view class."""
    view_class = GetCTypeDetails

    def test_view(self):
        resp = self.is_callable(data={'pk': 1, })
        ctype = ContentType.objects.get(pk=1)
        self.assertIn(ctype.app_label, resp.content.decode('utf-8'), msg=(
            'Should return a JSON string containing app_label and model'))

    def test_bad_pk(self):
        self.is_not_callable(data={'pk': 999, })
