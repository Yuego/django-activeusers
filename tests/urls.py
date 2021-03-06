"""URLs to run the tests."""
from django.urls import include, re_path
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^tracking/', include('activeusers.urls', namespace='activeusers')),
]
