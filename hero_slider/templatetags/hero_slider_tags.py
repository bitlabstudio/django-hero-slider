"""Templatetags for the ``hero_slider`` app."""
from django import template

from ..models import SliderItem


register = template.Library()


@register.assignment_tag(takes_context=True)
def get_slider_items(context, amount=None):
    """Returns the published slider items."""
    req = context.get('request')
    qs = SliderItem.objects.published(req).order_by('position')
    if amount:
        qs = qs[:amount]
    return qs


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
