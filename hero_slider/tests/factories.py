"""Factories for the ``hero_slider`` app."""
import factory

from filer.models.imagemodels import Image

from hero_slider.models import SliderItem, SliderItemTitle
from hero_slider.tests.test_app.models import DummyModel


class DummyModelFactory(factory.Factory):
    """Factory for ``DummyModel`` objects."""
    FACTORY_FOR = DummyModel

    name = 'A name'


class FilerImageFactory(factory.Factory):
    """Factory for ``Image`` objects of the django-filer app."""
    FACTORY_FOR = Image

    owner = None
    original_filename = 'foobar.jpg'
    file = None


class SliderItemFactory(factory.Factory):
    """Factory for ``SliderItem`` objects."""
    FACTORY_FOR = SliderItem

    image = factory.SubFactory(FilerImageFactory)
    content_object = factory.SubFactory(DummyModelFactory)


class SliderItemTitleFactoryBase(factory.Factory):
    """Base class for ``SliderItemTitle`` factories."""
    FACTORY_FOR = SliderItemTitle

    slider_item = factory.SubFactory(SliderItemFactory)


class SliderItemTitleENFactory(SliderItemTitleFactoryBase):
    """Factory for english ``SliderItemTitle`` objects."""
    title = 'A title'
    description = 'A description'
    language = 'en'
    is_published = True


class SliderItemTitleDEFactory(SliderItemTitleFactoryBase):
    """Factory for german ``SliderItemTitle`` objects."""
    title = 'Ein Titel'
    description = 'Eine Beschreibung'
    language = 'de'
    is_published = True
