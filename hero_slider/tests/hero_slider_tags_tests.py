"""Tests for the templatetags of the ``hero_slider`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory

from hero_slider.templatetags.hero_slider_tags import render_hero_slider
from hero_slider.tests.factories import (
    SliderItemTitleDEFactory,
    SliderItemTitleENFactory,
)


class RenderHeroSliderTestCase(TestCase):
    """Tests for the ``render_hero_slider`` templatetag."""
    longMessage = True

    def setUp(self):
        self.de_title = SliderItemTitleDEFactory()
        SliderItemTitleENFactory(
            slider_item=self.de_title.slider_item, is_published=False)
        self.en_title = SliderItemTitleENFactory()
        SliderItemTitleDEFactory(
            slider_item=self.en_title.slider_item, is_published=False)

    def test_tag(self):
        req = RequestFactory().get('/')
        req.LANGUAGE_CODE = 'en'
        context = RequestContext(req)
        result = render_hero_slider(context)

        self.assertEqual(len(result['slider_items']), 1, msg=(
            'When set to English, it should return one item.'))
        self.assertEqual(
            result['slider_items'][0], self.en_title.slider_item, msg=(
                'When set to English, it should return the english item.'))

        req.LANGUAGE_CODE = 'de'
        context = RequestContext(req)
        result = render_hero_slider(context)
        self.assertEqual(len(result['slider_items']), 1, msg=(
            'When set to German, it should return one item.'))
        self.assertEqual(
            result['slider_items'][0], self.de_title.slider_item, msg=(
                'When set to English, it should return the german item.'))

        req = RequestFactory().get('/')
        context = RequestContext(req)
        result = render_hero_slider(context)
        self.assertEqual(len(result['slider_items']), 0, msg=(
            'When no language is set, it should return no items.'))
