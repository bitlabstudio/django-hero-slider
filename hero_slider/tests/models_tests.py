"""Tests for the models of the ``hero_slider`` app."""
from django.test import TestCase

from hero_slider.tests.factories import (
    FilerImageFactory,
    SliderItemFactory,
    SliderItemTitleENFactory,
)


class SliderItemTestCase(TestCase):
    """Tests for the ``SliderItem`` model."""
    longMessage = True

    def test_model(self):
        foo = FilerImageFactory()
        instance = SliderItemFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))


class SliderItemTitleTestCase(TestCase):
    """Tests for the ``SliderItemTitle`` model."""
    longMessage = True

    def test_model(self):
        instance = SliderItemTitleENFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))
