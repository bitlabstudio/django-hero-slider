"""Tests for the models of the ``hero_slider`` app."""
from django.test import TestCase

from .factories import (
    SliderItemFactory,
    SliderItemCategoryFactory,
)


class SliderItemCategoryTestCase(TestCase):
    """Tests for the ``SliderItemCategory`` model."""
    longMessage = True

    def test_model(self):
        instance = SliderItemCategoryFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model'))


class SliderItemTestCase(TestCase):
    """Tests for the ``SliderItem`` model."""
    longMessage = True

    def test_model(self):
        instance = SliderItemFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))
