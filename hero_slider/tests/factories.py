# -*- coding: utf-8 -*-
"""Factories for the ``hero_slider`` app."""
import factory

from django_libs.tests.factories import HvadFactoryMixin
from filer.models.imagemodels import Image

from .. import models
from .test_app.models import DummyModel


class DummyModelFactory(factory.DjangoModelFactory):
    """Factory for ``DummyModel`` objects."""
    FACTORY_FOR = DummyModel

    name = 'A name'


class FilerImageFactory(factory.DjangoModelFactory):
    """Factory for ``Image`` objects of the django-filer app."""
    FACTORY_FOR = Image

    owner = None
    original_filename = 'foobar.jpg'
    file = None


class SliderItemCategoryFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for ``SliderItemCategory`` objects."""
    FACTORY_FOR = models.SliderItemCategory

    # for recent unicode errors, we added an 'Umlaut'
    name = factory.Sequence(lambda n: 'näme {0}'.format(n))


class SliderItemFactory(factory.DjangoModelFactory):
    """Factory for ``SliderItem`` objects."""
    FACTORY_FOR = models.SliderItem

    image = factory.SubFactory(FilerImageFactory)
    content_object = factory.SubFactory(DummyModelFactory)
    title = factory.Sequence(lambda n: 'title {0}'.format(n))
    description = factory.Sequence(lambda n: 'description {0}'.format(n))
    is_published = True
    language_code = 'en'
