from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    pass


class ResearchPage(TemplateView):
    pass


class ItemDetailPage(TemplateView):
    template_name = 'dashboard/item_detail.html'

