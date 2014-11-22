from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    pass


class ResearchPage(TemplateView):
    template_name = 'dashboard/research_list.html'


class ItemDetailPage(TemplateView):
    template_name = 'dashboard/item_detail.html'

