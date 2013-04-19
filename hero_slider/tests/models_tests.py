"""Tests for the models of the ``hero_slider`` app."""
from mock import Mock

from django.test import TestCase

from ..models import SliderItem
from .factories import (
    SliderItemFactory,
    SliderItemTitleDEFactory,
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


class SliderItemManagerTestCase(TestCase):
    """Tests for the ``SliderItemManager`` model manager."""
    longMessage = True

    def setUp(self):
        self.en_title = SliderItemTitleENFactory(is_published=False)
        SliderItemTitleDEFactory(slider_item=self.en_title.slider_item)

        self.de_title = SliderItemTitleDEFactory(is_published=False)
        SliderItemTitleENFactory(slider_item=self.de_title.slider_item)

    def test_manager(self):
        """Test if the ``SliderItemManager`` retrieves the correct objects."""
        request = Mock(LANGUAGE_CODE='de')
        self.assertEqual(
            SliderItem.objects.published(request).count(), 1, msg=(
                'In German, there should be one published slider item.'))

        request = Mock(LANGUAGE_CODE='en')
        self.assertEqual(
            SliderItem.objects.published(request).count(), 1, msg=(
                'In English, there should be one published slider item.'))

        request = Mock(LANGUAGE_CODE=None)
        self.assertEqual(
            SliderItem.objects.published(request).count(), 0, msg=(
                'If no language is set, there should be no slider items.'))


class SliderItemTitleTestCase(TestCase):
    """Tests for the ``SliderItemTitle`` model."""
    longMessage = True

    def test_model(self):
        instance = SliderItemTitleENFactory()
        self.assertTrue(instance.pk, msg=(
            'Should be able to instantiate and save the model.'))
