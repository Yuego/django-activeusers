# -*- coding: utf-8 -*-

try:
    from django.apps import AppConfig
except ImportError:
    pass  # Django < 1.7
else:

    class Config(AppConfig):
        name = 'activeusers'
        try:
            from . import __version__ as version_info
        except:
            version_info = 'n/a'
        verbose_name = 'Active Users (' + version_info + ')'
