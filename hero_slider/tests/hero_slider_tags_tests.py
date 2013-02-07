"""Tests for the templatetags of the ``hero_slider`` app."""
from django.test import TestCase

from hero_slider.templatetags.hero_slider_tags import render_hero_slider
from hero_slider.tests.factories import SliderItemFactory


class RenderHeroSliderTestCase(TestCase):
    """Tests for the ``render_hero_slider`` templatetag."""
    def test_tag(self):
        SliderItemFactory()
        SliderItemFactory()
        SliderItemFactory()
        result = render_hero_slider()
        self.assertEqual(len(result['slider_items']), 3)
