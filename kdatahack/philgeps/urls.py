from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    BiddersListLAPI,
    AwardsLAPI,
    OrganizationLAPI,
    BidLineItemLAPI,
    BidInformationLAPI,
    BiddersListRAPI,
    AwardsRAPI,
    OrganizationRAPI,
    BidLineItemRAPI,
    BidInformationRAPI,
)


# NOTE:
# Accessed via /api/v1/philgeps/<resource>
# or via named urls 'api_v1:<resource>'
urlpatterns = patterns(
    '',
    url(
        r'^bidderslist$',
        BiddersListLAPI.as_view(),
        name='bidderslist',
    ),
    url(
        r'^bidderslist/(?P<pk>\d+)$',
        BiddersListRAPI.as_view(),
        name='bidderslist_get',
    ),
    url(
        r'^awards$',
        AwardsLAPI.as_view(),
        name='awards',
    ),
    url(
        r'^awards/(?P<pk>\d+)$',
        AwardsRAPI.as_view(),
        name='awards_get',
    ),
    url(
        r'^organization$',
        OrganizationLAPI.as_view(),
        name='organization',
    ),
    url(
        r'^organization/(?P<pk>\d+)$',
        OrganizationRAPI.as_view(),
        name='organization_get',
    ),
    url(
        r'^bidlineitem$',
        BidLineItemLAPI.as_view(),
        name='bidlineitem',
    ),
    url(
        r'^bidlineitem/(?P<pk>\d+)$',
        BidLineItemRAPI.as_view(),
        name='bidlineitem_get',
    ),
    url(
        r'^bidinformation$',
        BidInformationLAPI.as_view(),
        name='bidinformation',
    ),
    url(
        r'^bidinformation/(?P<pk>\d+)$',
        BidInformationRAPI.as_view(),
        name='bidinformation_get',
    ),
)
