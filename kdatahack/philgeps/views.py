from django.shortcuts import render

from rest_framework import filters
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
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'award_id',
        'line_item_id',
        'org_id',
        'bidder_name',
    )


class AwardsLAPI(ListAPIView):
    model = Awards
    serializer_class = AwardsSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'award_id',
        'ref_id',
        'award_title',
        'publish_date',
        'previous_award_id',
        'line_item_id',
        'item_name',
        'item_description',
        'quantity',
        'uom',
        'budget',
        'unspc_code',
        'unspc_description',
        'awardee_id',
        'awardee',
        'award_type',
        'contract_amt',
        'award_date',
        'award_reason',
        'contract_no',
        'proceed_date',
        'contract_start_date',
        'contract_end_date',
        'is_short_list',
        'is_re_award',
        'is_amp',
    )


class OrganizationLAPI(ListAPIView):
    model = Organization
    serializer_class = OrganizationSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'org_id',
        'member_type_id',
        'member_type',
        'parent_org_id',
        'is_org_foreign',
        'org_name',
        'goverment_branch',
        'government_organization_type',
        'supplier_form_of_organization',
        'supplier_organization_type',
        'org_reg_date',
        'website',
        'org_description',
        'country_code',
        'country',
        'region',
        'province',
        'city',
        'address1',
        'address2',
        'address3',
        'zip_code',
        'org_status',
        'modified_date',
    )


class BidLineItemLAPI(ListAPIView):
    model = BidLineItem
    serializer_class = BidLineItemSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'ref_id',
        'line_item_id',
        'item_name',
        'item_description',
        'qty',
        'uomid',
        'uom',
        'budget',
        'modified_date',
    )


class BidInformationLAPI(ListAPIView):
    model = BidInformation
    serializer_class = BidInformationSerializer
    paginate_by = 10
    max_paginate_by = 100
    paginate_by_param = 'page_size'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'ref_id',
        'ref_no',
        'stage',
        'stage2_ref_id',
        'org_id',
        'classification',
        'solicitation_no',
        'notice_type',
        'business_category',
        'procurement_mode',
        'funding_instrument',
        'funding_source',
        'approved_budget',
        'publish_date',
        'closing_date',
        'contract_duration',
        'calendar_type',
        'trade_agreement',
        'pre_bid_date',
        'pre_bid_venue',
        'procuring_entity_org_id',
        'procuring_entity_org',
        'client_agency_org_id',
        'client_agency_org',
        'contact_person',
        'contact_person_address',
        'tender_title',
        'description',
        'other_info',
        'tender_status',
        'reason',
        'date_available',
        'collection_contact',
        'collection_point',
        'special_instruction',
        'created_by',
        'creation_date',
        'modified_date',
    )


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
