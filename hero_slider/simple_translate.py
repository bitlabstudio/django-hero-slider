"""Registering translated models for the ``hero_slider`` app."""
from simple_translation.translation_pool import translation_pool

from hero_slider.models import (
    SliderItem,
    SliderItemTitle,
)


translation_pool.register_translation(SliderItem, SliderItemTitle)
