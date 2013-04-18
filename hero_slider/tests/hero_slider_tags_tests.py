"""Tests for the templatetags of the ``hero_slider`` app."""
from django.template import RequestContext
from django.test import TestCase, RequestFactory

from hero_slider.templatetags.hero_slider_tags import render_hero_slider
from hero_slider.tests.factories import SliderItemTitleDEFactory


class RenderHeroSliderTestCase(TestCase):
    """Tests for the ``render_hero_slider`` templatetag."""
    longMessage = True

    def setUp(self):
        SliderItemTitleDEFactory()
        SliderItemTitleDEFactory()
        SliderItemTitleDEFactory()

    def test_tag(self):
        req = RequestFactory().get('/')
        context = RequestContext(req)
        result = render_hero_slider(context)
        self.assertEqual(len(result['slider_items']), 3)
