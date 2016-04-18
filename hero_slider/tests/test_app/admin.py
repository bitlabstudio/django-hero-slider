"""Admin classes for the ``hero_slider`` test-app."""
from django.contrib import admin

from .models import DummyModel


admin.site.register(DummyModel)
