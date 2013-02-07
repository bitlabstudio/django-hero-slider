"""Models for the ``hero_slider`` app."""
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from simple_translation.utils import get_translation_queryset


from filer.fields.file import FilerFileField


class SliderItem(models.Model):
    """
    Resembles an item that should be shown on the front page in a slider.

    For translateable fields see the ``SliderItemTitle`` model.

    :image: A filer file. This will be the image shown in the slider.
    :position: Can be set in order to control the ordering of the slider items.
    :content_type: The contenttype of the object this slider item links to.
    :object_id: The PK of the object this slider item links to.

    """
    image = FilerFileField(
        verbose_name=_('Image'),
    )

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        null=True, blank=True,
    )

    # Generic foreign key
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def get_trans(self):
        """Returns the translation object for this slider item."""
        lang = get_language()
        return get_translation_queryset(self).filter(language=lang)[0]


class SliderItemTitle(models.Model):
    """
    Translateable fields of the ``SliderItem`` model.

    :title: The title of this slider item.
    :description: A short description of this slider item.

    """
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
        blank=True,
    )

    description = models.CharField(
        max_length=512,
        verbose_name=_('Description'),
        blank=True,
    )

    # Needed by simple-translation
    slider_item = models.ForeignKey(SliderItem, verbose_name=_('Slider item'))
    language = models.CharField(max_length=2, verbose_name=_('Language'))
