"""Registering translated models for the ``hero_slider`` app."""
from simple_translation.translation_pool import translation_pool

from . import models


translation_pool.register_translation(
    models.SliderItem, models.SliderItemTitle)
translation_pool.register_translation(
    models.SliderItemCategory, models.SliderItemCategoryTitle)
