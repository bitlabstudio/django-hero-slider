"""Admin classes for the ``hero_slider`` app."""
from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from django_libs.admin import MultilingualPublishMixin
from simple_translation.admin import TranslationAdmin
from simple_translation.utils import get_preferred_translation_from_lang

from hero_slider.models import SliderItem


class SliderItemAdmin(MultilingualPublishMixin, TranslationAdmin):
    """Admin for the ``SliderItem`` model."""
    list_display = ['title', 'position', 'languages', 'is_published']

    def title(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).title
    title.short_description = _('Title')


admin.site.register(SliderItem, SliderItemAdmin)
