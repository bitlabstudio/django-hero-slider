"""URLs for the ``hero_slider`` app."""
from django.conf.urls.defaults import patterns, url

from hero_slider.views import GetCTypeDetails


urlpatterns = patterns(
    '',
    url(r'ctype/$', GetCTypeDetails.as_view(), name='get_ctype_details'),
)
