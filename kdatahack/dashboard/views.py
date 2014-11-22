from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404

from masteritems.models import MasterItem


class HomePage(TemplateView):
    template_name = 'dashboard/home.html'


class ResearchPage(TemplateView):
    template_name = 'dashboard/research_list.html'


class ItemDetailPage(TemplateView):
    template_name = 'dashboard/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailPage, self).get_context_data(**kwargs)
        try:
            mitem = MasterItem.objects.get(pk=kwargs.get('item_id'))
        except:
            raise Http404
        context['item'] = mitem
        return context
