from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    MasterItemLAPI,
    MasterItemRAPI,
)


# NOTE:
# Accessed via /api/v1/masterlist/<resource>
# or via named urls 'api_v1:<resource>'
urlpatterns = patterns(
    '',
    url(
        r'^masteritem$',
        MasterItemLAPI.as_view(),
        name='masteritem',
    ),
    url(
        r'^masteritem/(?P<pk>\d+)$',
        MasterItemRAPI.as_view(),
        name='masteritem_get',
    ),
)
