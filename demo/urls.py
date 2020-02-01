from django.conf import settings
from django.urls import re_path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    re_path(r'^activeusers/', 'activeusers.urls'),
    re_path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'static/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    ]
