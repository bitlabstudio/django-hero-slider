"""Dummy models for the tests of the ``hero_slider`` app."""
from django.db import models


class DummyModel(models.Model):
    """DummyModel for tests of the ``hero_slider`` app."""
    name = models.CharField(max_length=256)
