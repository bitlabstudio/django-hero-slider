"""Tests for the models of the ``hero_slider`` app."""
from django.test import TestCase

from mixer.backend.django import mixer


class SliderItemCategoryTestCase(TestCase):
    """Tests for the ``SliderItemCategory`` model."""
    longMessage = True

    def test_model(self):
        instance = mixer.blend('hero_slider.SliderItemCategory')
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model'))


class SliderItemTestCase(TestCase):
    """Tests for the ``SliderItem`` model."""
    longMessage = True

    def setUp(self):
        self.instance = mixer.blend('hero_slider.SliderItem')

    def test_model(self):
        self.assertTrue(self.instance.pk, msg=(
            'Should be able to instantiate and save the model.'))

    def test_get_item_url(self):
        self.assertEqual(
            self.instance.get_item_url(), self.instance.external_url, msg=(
                'Should return the etxernal URL.'))
