"""Tests for the views of the ``hero_slider`` app."""
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.test import RequestFactory, TestCase

from hero_slider.views import GetCTypeDetails


class GetCTypeDetailsTestCase(TestCase):
    """Tests for the ``GetCTypeDetails`` view class."""
    def test_view(self):
        req = RequestFactory().get('/')
        req.GET = {'pk': 1, }
        resp = GetCTypeDetails.as_view()(req)
        ctype = ContentType.objects.get(pk=1)
        self.assertTrue(ctype.app_label in resp.content, msg=(
            'Should return a JSON string containing app_label and model'))

    def test_bad_pk(self):
        req = RequestFactory().get('/')
        req.GET = {'pk': 999, }
        self.assertRaises(Http404, GetCTypeDetails.as_view(), req)
