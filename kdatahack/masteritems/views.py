from django.shortcuts import render

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
