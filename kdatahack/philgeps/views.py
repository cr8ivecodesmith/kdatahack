from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)


from .models import (
    BiddersList,
    Awards,
    Organization,
    BidLineItem,
    BidInformation,
)
from .serializers import (
    BiddersListSerializer,
    AwardsSerializer,
    OrganizationSerializer,
    BidLineItemSerializer,
    BidInformationSerializer,
)


class BiddersListLAPI(ListAPIView):
    model = BiddersList
    serializer_class = BiddersListSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'


class AwardsLAPI(ListAPIView):
    model = Awards
    serializer_class = AwardsSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'


class OrganizationLAPI(ListAPIView):
    model = Organization
    serializer_class = OrganizationSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'


class BidLineItemLAPI(ListAPIView):
    model = BidLineItem
    serializer_class = BidLineItemSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'


class BidInformationLAPI(ListAPIView):
    model = BidInformation
    serializer_class = BidInformationSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'


class BiddersListRAPI(RetrieveAPIView):
    model = BiddersList
    serializer_class = BiddersListSerializer


class AwardsRAPI(RetrieveAPIView):
    model = Awards
    serializer_class = AwardsSerializer


class OrganizationRAPI(RetrieveAPIView):
    model = Organization
    serializer_class = OrganizationSerializer


class BidLineItemRAPI(RetrieveAPIView):
    model = BidLineItem
    serializer_class = BidLineItemSerializer


class BidInformationRAPI(RetrieveAPIView):
    model = BidInformation
    serializer_class = BidInformationSerializer
