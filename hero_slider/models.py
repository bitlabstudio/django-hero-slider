"""Models for the ``hero_slider`` app."""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_libs.models_mixins import (
    HvadPublishedManager, TranslationModelMixin)
from filer.fields.file import FilerFileField
from hvad.models import TranslatedFields, TranslatableModel


class SliderItemCategory(TranslationModelMixin, TranslatableModel):
    """
    Each slider item can belong to a category.

    :slug: The slug of this category.

    translated:
    :name: The name of this category

    """
    slug = models.SlugField(
        max_length=128,
        verbose_name=_('Slug'),
    )
    translations = TranslatedFields(
        name=models.CharField(
            max_length=128,
            verbose_name=_('Name'),
        )
    )


class SliderItem(TranslationModelMixin, TranslatableModel):
    """
    Resembles an item that should be shown on the front page in a slider.

    For translateable fields see the ``SliderItemTitle`` model.

    :category: The category of this item (optional)
    :image: A filer file. This will be the image shown in the slider.
    :position: Can be set in order to control the ordering of the slider items.
    :content_type: The contenttype of the object this slider item links to.
    :object_id: The PK of the object this slider item links to.
    :external_url: URL to link to items without the need of a gfk.
    :text_position_top: Text position.
    :text_position_bottom: Text position.
    :text_position_left: Text position.
    :text_position_right: Text position.

    translated:
    :title: The title of this slider item.
    :description: A short description of this slider item.
    :link_text: If you want to render a call to action button on the slide,
      you can define the link text here.
    :is_published: If True, this will not show up.

    """
    category = models.ForeignKey(
        SliderItemCategory,
        verbose_name=_('Category'),
        null=True, blank=True,
    )

    image = FilerFileField(
        verbose_name=_('Image'),
    )

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        null=True, blank=True,
    )

    # Generic foreign key
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    external_url = models.CharField(
        verbose_name=_('External URL'),
        max_length=512,
        blank=True,
    )

    text_position_top = models.IntegerField(
        verbose_name=_('Text position top'),
        blank=True, null=True,
    )

    text_position_bottom = models.IntegerField(
        verbose_name=_('Text position bottom'),
        blank=True, null=True,
    )

    text_position_left = models.IntegerField(
        verbose_name=_('Text position left'),
        blank=True, null=True,
    )

    text_position_right = models.IntegerField(
        verbose_name=_('Text position right'),
        blank=True, null=True,
    )

    translations = TranslatedFields(
        title=models.CharField(
            max_length=256,
            verbose_name=_('Title'),
            blank=True,
        ),
        description=models.CharField(
            max_length=512,
            verbose_name=_('Description'),
            blank=True,
        ),
        link_text=models.CharField(
            max_length=512,
            verbose_name=_('Link text'),
            blank=True,
        ),
        is_published=models.BooleanField(
            verbose_name=_('Is published'),
            default=False,
        )
    )

    objects = HvadPublishedManager()

    def get_item_url(self):
        """Returns the url of the connected item."""
        try:
            return self.content_object.get_absolute_url()
        except AttributeError:
            return self.external_url
