# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

from wgame.views import version_control_view

urlpatterns = patterns(
    '',
    # url('^version/(?P<game_name>[-_a-zA-Z0-9]+)/(?P<version>[-_a-zA-Z0-9]+)/(?P<switch>[0-9]+)/?$', version_control_view),
    url('^version/([-_a-zA-Z0-9]+)/([-_a-zA-Z0-9\.]+)/([0-1])/?$', version_control_view),
    # url('^get_version/?$', get_version_control_view),
)
