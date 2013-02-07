"""Admin classes for the ``hero_slider`` test-app."""
from django.contrib import admin

from hero_slider.tests.test_app.models import DummyModel


admin.site.register(DummyModel)
