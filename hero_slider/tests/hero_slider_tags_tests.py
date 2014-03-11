"""Tests for the templatetags of the ``hero_slider`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory

from hero_slider.templatetags.hero_slider_tags import (
    get_slider_items,
    render_hero_slider,
)
from hero_slider.tests.factories import SliderItemFactory


class GetSliderItemsTestCase(TestCase):
    """Tests for the ``get_slider_items`` templatetag."""
    longMessage = True

    def test_tag(self):
        SliderItemFactory()
        req = RequestFactory().get('/')
        req.LANGUAGE_CODE = 'en'
        context = RequestContext(req)
        result = get_slider_items(context)
        self.assertEqual(result.count(), 1, msg=(
            'Should return the published slider items.'))


class RenderHeroSliderTestCase(TestCase):
    """Tests for the ``render_hero_slider`` templatetag."""
    longMessage = True

    def setUp(self):
        self.de_item = SliderItemFactory(language_code='de')
        new_item = self.de_item.translate('en')
        new_item.is_published = False
        new_item.save()

        self.en_item = SliderItemFactory()
        new_item = self.en_item.translate('de')
        new_item.is_published = False
        new_item.save()

    def test_tag(self):
        req = RequestFactory().get('/')
        req.LANGUAGE_CODE = 'en'
        context = RequestContext(req)
        result = render_hero_slider(context)

        self.assertEqual(len(result['slider_items']), 1, msg=(
            'When set to English, it should return one item.'))
        self.assertEqual(
            result['slider_items'][0], self.en_item, msg=(
                'When set to English, it should return the english item.'))

        req.LANGUAGE_CODE = 'de'
        context = RequestContext(req)
        result = render_hero_slider(context)
        self.assertEqual(len(result['slider_items']), 1, msg=(
            'When set to German, it should return one item.'))
        self.assertEqual(
            result['slider_items'][0], self.de_item, msg=(
                'When set to English, it should return the german item.'))

        req = RequestFactory().get('/')
        context = RequestContext(req)
        result = render_hero_slider(context)
        self.assertEqual(len(result['slider_items']), 0, msg=(
            'When no language is set, it should return no items.'))
