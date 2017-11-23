"""Tests for the models of the activeusers app."""
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User

from activeusers.middleware import VisitorTrackingMiddleware
from activeusers.models import Visitor


class VisitorTrackingMiddlewareTestCase(TestCase):
    """Tests for the ``Visitor`` model."""

    def setUp(self):
        self.mw = VisitorTrackingMiddleware()
        self.factory = RequestFactory()

    def test_model(self):
        url = '/admin/'
        self.assertEquals(Visitor.objects.count(), 0)

        request = self.factory.get(url)
        request.user = AnonymousUser()
        self.mw.process_request(request)

        self.assertEquals(Visitor.objects.count(), 1)

        current_visitor = Visitor.objects.all().latest('id')
        self.assertEquals(current_visitor.page_views, 1)
        self.assertEquals(current_visitor.url, url)
