# -*- coding: utf-8 -*-
from django.conf.urls import url
from activeusers import views

app_name = 'activeusers'

urlpatterns = [
    url(r'^refresh/$',
        views.update_active_users,
        name='activeusers-refresh-active-users', ),
    url(r'^refresh/json/$',
        views.get_active_users,
        name='activeusers-get-active-users', ),
]
