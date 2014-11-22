from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns(
    '',
    url(r'$', views.HomePage.as_view(), name='dashboard_home_page'),
    url(r'^research/$', views.ResearchPage.as_view(), name='dashboard_research_page'),
    url(r'^item/(?P<item_id>\d+)/$', views.ItemDetailPage.as_view(), name='dashboard_item_detail_page'),
)

