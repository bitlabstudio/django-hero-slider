"""Tests for the models of the ``hero_slider`` app."""
from django.test import TestCase

from hero_slider.tests.factories import (
    SliderItemFactory,
    SliderItemTitleENFactory,
)


class SliderItemTestCase(TestCase):
    """Tests for the ``SliderItem`` model."""
    longMessage = True

    def test_model(self):
        instance = SliderItemFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))

    def test_get_trans(self):
        item_trans = SliderItemTitleENFactory()
        self.assertEqual(item_trans.slider_item.get_trans(), item_trans, msg=(
            'Should return the translation object for the current language'))


class SliderItemTitleTestCase(TestCase):
    """Tests for the ``SliderItemTitle`` model."""
    longMessage = True

    def test_model(self):
        instance = SliderItemTitleENFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))
