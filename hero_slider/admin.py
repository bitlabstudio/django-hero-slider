"""Admin classes for the ``hero_slider`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from hvad.admin import TranslatableAdmin

from . import models


class SliderItemCategoryAdmin(TranslatableAdmin):
    """Admin for the ``SliderItemCategory`` model."""
    list_display = ['slug', 'get_name', 'all_translations']

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


class SliderItemAdmin(TranslatableAdmin):
    """Admin for the ``SliderItem`` model."""
    list_display = ['get_title', 'position', 'all_translations',
                    'get_is_published']
    list_editable = ['position', ]

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')

    def get_is_published(self, obj):
        return obj.is_published
    get_is_published.short_description = _('Is published')
    get_is_published.boolean = True


admin.site.register(models.SliderItem, SliderItemAdmin)
admin.site.register(models.SliderItemCategory, SliderItemCategoryAdmin)
