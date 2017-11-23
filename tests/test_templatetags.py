"""Tests for the models of the activeusers app."""
from django.test import TestCase

from activeusers.templatetags.tracking_tags import visitors_on_page


class TemplatetagsTestCase(TestCase):
    """Tests for the ``Visitor`` model."""

    def test_visitors_on_page(self):
        pass
        # visitors_on_page('', '')
