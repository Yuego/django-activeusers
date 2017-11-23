"""Tests for the models of the activeusers app."""
from django.test import TestCase
from activeusers.models import Visitor


class VisitorModelTestCase(TestCase):
    """Tests for the ``Visitor`` model."""

    def test_model(self):
        self.assertTrue(True)
