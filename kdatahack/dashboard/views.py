from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse, Http404
from itertools import izip
import tablib

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


class ReportPage(View):
   
    def get(self, request, *args, **kwargs):
        print request
        items = request.GET.getlist('items', [])
        qtys = request.GET.getlist('qtys', [])
        table = tablib.Dataset()
        table.headers = ['Item Name', 'Item Description', 'Price', 'Quantity', 'UOM', 'Total']
        grand_total = 0
        for item, qty in izip(items, qtys):
            master = MasterItem.objects.get(pk=item)
            total = float(master.market_price) * float(qty)
            table.append([
                master.item_name,
                master.item_description,
                master.market_price,
                qty,
                master.uom,
                total])
            grand_total += total
        table.append(['','','','','GRAND TOTAL', grand_total])
        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="MarketResearch.csv"'
        response.write(table.csv)
        return response

