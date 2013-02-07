"""Templatetags for the ``hero_slider`` app."""
from django import template

from hero_slider.models import SliderItem


register = template.Library()


@register.inclusion_tag('hero_slider/carousel.html')
def render_hero_slider():
    """
    Renders the hero slider.

    """
    qs = SliderItem.objects.all().order_by('position')
    return {
        'slider_items': qs,
    }
