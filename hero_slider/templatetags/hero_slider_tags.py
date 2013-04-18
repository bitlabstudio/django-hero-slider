"""Templatetags for the ``hero_slider`` app."""
from django import template

from hero_slider.models import SliderItem


register = template.Library()


@register.inclusion_tag('hero_slider/carousel.html', takes_context=True)
def render_hero_slider(context):
    """
    Renders the hero slider.

    """
    req = context.get('request')
    qs = SliderItem.objects.published(req).order_by('position')
    return {
        'slider_items': qs,
    }
