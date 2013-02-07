"""Views for the ``hero_slider`` app."""
import json

from django.contrib.contenttypes.models import ContentType
from django.views.generic import View
from django.http import Http404, HttpResponse


class GetCTypeDetails(View):
    """Returns the app name for a given content type PK as a JSON response."""
    def get(self, request, *args, **kwargs):
        try:
            ctype = ContentType.objects.get(pk=request.GET.get('pk'))
        except ContentType.DoesNotExist:
            raise Http404
        context = {
            'app_label': ctype.app_label,
            'model': ctype.model,
        }
        response_kwargs = {}
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(json.dumps(context), **response_kwargs)
