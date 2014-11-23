from django.shortcuts import render

from eztables.views import DatatablesView
from rest_framework import filters
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .models import MasterItem
from .serializers import MasterItemSerializer


class MasterItemLAPI(ListAPIView):
    model = MasterItem
    serializer_class = MasterItemSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'item_name',
        'item_description',
        'uom',
    )


class MasterItemRAPI(RetrieveAPIView):
    model = MasterItem
    serializer_class = MasterItemSerializer


class MasterItemDatatable(DatatablesView):
    model = MasterItem
    fields = (
        'id',
        'item_name',
        'item_description',
        'uom',
    )

    def get_rows(self, rows):
        rows = super(MasterItemDatatable, self).get_rows(rows)
        new_rows = []
        for row in rows:
            row.append(self.get_market_price(row))  # Index 5
            new_rows.append(row)
        return new_rows

    def get_market_price(self, row):
        price = self.model.objects.get(pk=row[0])._get_market_price()
        return price
