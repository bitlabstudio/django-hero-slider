"""Models for the ``hero_slider`` app."""
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from django_libs.models_mixins import SimpleTranslationMixin
from simple_translation.utils import get_preferred_translation_from_lang


from filer.fields.file import FilerFileField


class SliderItemCategory(SimpleTranslationMixin, models.Model):
    """
    Each slider item can belong to a category.

    :slug: The slug of this category.

    """
    slug = models.SlugField(
        max_length=128,
        verbose_name=_('Slug'),
    )

    def __unicode__(self):
        return self.get_translation().name


class SliderItemCategoryTitle(models.Model):
    """
    Translateable fields for the SliderItemCategory model.

    :name: The name of this category
    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Name'),
    )

    # Needed by simple-translation
    slider_item_category = models.ForeignKey(
        SliderItemCategory,
        verbose_name=_('Slider item category'),
    )
    language = models.CharField(max_length=5, verbose_name=_('Language'))


class SliderItemManager(models.Manager):
    """Custom manager for the ``SliderItem`` model."""
    def published(self, request):
        """
        Returns the published slider items in the current language.

        :param request: A Request instance.

        """
        language = getattr(request, 'LANGUAGE_CODE', None)
        if not language:
            return self.model.objects.none()
        qs = self.get_query_set()
        qs = qs.filter(
            slideritemtitle__is_published=True,
            slideritemtitle__language=language,
        )
        return qs


class SliderItem(models.Model):
    """
    Resembles an item that should be shown on the front page in a slider.

    For translateable fields see the ``SliderItemTitle`` model.

    :category: The category of this item (optional)
    :image: A filer file. This will be the image shown in the slider.
    :position: Can be set in order to control the ordering of the slider items.
    :content_type: The contenttype of the object this slider item links to.
    :object_id: The PK of the object this slider item links to.
    :external_url: URL to link to items without the need of a gfk.

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
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    external_url = models.CharField(
        verbose_name=_('External URL'),
        max_length=512,
        blank=True,
    )

    objects = SliderItemManager()

    def get_trans(self):
        """Returns the translation object for this slider item."""
        lang = get_language()
        return get_preferred_translation_from_lang(self, lang)

    def get_item_url(self):
        """Returns the url of the connected item."""
        try:
            return self.content_object.get_absolute_url()
        except AttributeError:
            return self.external_url


class SliderItemTitle(models.Model):
    """
    Translateable fields of the ``SliderItem`` model.

    :title: The title of this slider item.
    :description: A short description of this slider item.
    :is_published: If True, this will not show up.

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

    is_published = models.BooleanField(
        verbose_name=_('Is published'),
        default=False,
    )

    # Needed by simple-translation
    slider_item = models.ForeignKey(SliderItem, verbose_name=_('Slider item'))
    language = models.CharField(max_length=5, verbose_name=_('Language'))
