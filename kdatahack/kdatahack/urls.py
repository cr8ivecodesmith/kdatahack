from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    HomepageView,
    UserProfileView,
    UserProfileEditView,
    UserListAPIView,
    UserDetailsAPIView,
)

from dashboard.views import HomePage, ResearchPage, ItemDetailPage


api_v1_patterns = format_suffix_patterns(patterns(
    '',
    url(
        r'users/list',
        UserListAPIView.as_view(),
        name='users_list',
    ),
    url(
        r'users/details/(?P<username>\w+)',
        UserDetailsAPIView.as_view(),
        name='users_details',
    ),
    url(
        r'philgeps/',
        include('philgeps.urls'),
    ),
    url(
        r'masterlist/',
        include('masteritems.urls'),
    ),
))

urlpatterns = patterns(
    '',

    # Authentication URLs
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Third-party app URLs
    url(r'^djangojs/', include('djangojs.urls')),

    # Local app URLs
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^research/', ResearchPage.as_view(), name='research'),
    url(r'^item/(?P<item_id>\d+)/$', ItemDetailPage.as_view(), name='item_detail'),
    url(r'^(?P<username>\w+)/$', UserProfileView.as_view(), name='user_profile_view'),
    url(r'^(?P<username>\w+)/edit/$', UserProfileEditView.as_view(), name='user_profile_edit'),
    url(r'^api/v1/', include(api_v1_patterns, namespace='api_v1'))
)
