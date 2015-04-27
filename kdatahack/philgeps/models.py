from django.db import models

from django.contrib.contenttypes.models import ContentType

from core.models import SelfAwareModelMixin

from .managers import (
    OrganizationManager,
    BidInformationManager,
    BidLineItemManager,
    AwardsManager,
    BiddersListManager
)


class BiddersList(models.Model):
    award_id = models.ForeignKey('Awards', to_field='award_id', null=True)
    line_item_id = models.ForeignKey('BidLineItem', to_field='line_item_id', null=True)
    org_id = models.ForeignKey('Organization', to_field='org_id', null=True)
    bidder_name = models.CharField(max_length=2048)
    modified_date = models.DateTimeField(null=True)

    objects = BiddersListManager()


class Awards(models.Model):
    award_id = models.PositiveIntegerField(null=False, unique=True)
    ref_id = models.ForeignKey('BidInformation', to_field='ref_id', null=True)
    award_title = models.CharField(max_length=2048, blank=True)
    publish_date = models.DateTimeField(null=True)
    previous_award_id = models.PositiveIntegerField(null=True)
    line_item_id = models.ForeignKey('BidLineItem', to_field='line_item_id', null=True)
    item_name = models.CharField(max_length=2048, blank=True)
    item_description = models.TextField()
    quantity = models.PositiveIntegerField(null=True)
    uom = models.CharField(max_length=2048, blank=True)
    budget = models.FloatField()
    unspc_code = models.CharField(max_length=2048, blank=True)
    unspc_description = models.TextField()
    awardee_id = models.ForeignKey('Organization', to_field='org_id', null=True)
    awardee = models.CharField(max_length=2048, blank=True)
    award_type = models.CharField(max_length=2048, blank=True)
    contract_amt = models.FloatField()
    award_date = models.DateTimeField(null=True)
    award_reason = models.CharField(max_length=2048, blank=True)
    contract_no = models.CharField(max_length=2048, blank=True)
    proceed_date = models.DateTimeField(null=True)
    contract_start_date = models.DateTimeField(null=True)
    contract_end_date = models.DateTimeField(null=True)
    is_short_list = models.IntegerField(null=True)
    is_re_award = models.IntegerField(null=True)
    is_amp = models.IntegerField(null=True)

    master_item = models.ForeignKey('masteritems.MasterItem', related_name='awards_set', blank=True, null=True)

    def __unicode__(self):
     return "{}:{}".format(self.award_id, self.item_name)

    def _get_unit_price(self):
        if self.quantity:
            return self.contract_amt / self.quantity
        else:
            return self.contract_amt
    unit_price = property(_get_unit_price)

    objects = AwardsManager()


class Organization(models.Model, SelfAwareModelMixin):
    org_id = models.PositiveIntegerField(null=False, unique=True)
    member_type_id = models.PositiveIntegerField(null=True)
    member_type = models.CharField(max_length=2048, blank=True)
    parent_org_id = models.PositiveIntegerField(null=True)
    is_org_foreign = models.NullBooleanField()
    org_name = models.CharField(max_length=2048, blank=True)
    goverment_branch = models.CharField(max_length=2048, blank=True)
    government_organization_type = models.CharField(max_length=2048, blank=True)
    supplier_form_of_organization = models.CharField(max_length=2048, blank=True)
    supplier_organization_type = models.CharField(max_length=2048, blank=True)
    org_reg_date = models.DateTimeField(null=True)
    website = models.URLField(blank=True)
    org_description = models.TextField(blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    country = models.CharField(max_length=2048, blank=True)
    region = models.CharField(max_length=2048, blank=True)
    province = models.CharField(max_length=2048, blank=True)
    city = models.CharField(max_length=2048, blank=True)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    address3 = models.TextField(blank=True)
    zip_code = models.CharField(max_length=2048, blank=True)
    org_status = models.CharField(max_length=2048, blank=True)
    modified_date = models.DateTimeField(null=True)

    objects = OrganizationManager()


class BidInformation(models.Model, SelfAwareModelMixin):
    ref_id = models.IntegerField(unique=True)
    ref_no = models.CharField(blank=True, max_length=2048)  
    stage = models.IntegerField(null=True)
    stage2_ref_id = models.CharField(blank=True, max_length=2048)
    org_id = models.ForeignKey(Organization, to_field='org_id', related_name='bid_information', null=True)
    classification = models.CharField(blank=True, max_length=2048)
    solicitation_no = models.CharField(blank=True, max_length=2048)
    notice_type = models.CharField(blank=True, max_length=2048)
    business_category = models.CharField(blank=True, max_length=2048)
    procurement_mode = models.CharField(blank=True, max_length=2048)
    funding_instrument = models.CharField(blank=True, max_length=2048)
    funding_source = models.CharField(blank=True, max_length=2048)
    approved_budget = models.FloatField(null=True, blank=False)
    publish_date = models.DateTimeField(null=True, blank=False)
    closing_date = models.DateTimeField(null=True, blank=False)
    contract_duration = models.IntegerField(null=True)
    calendar_type = models.CharField(blank=True, max_length=2048)
    trade_agreement = models.CharField(blank=True, max_length=2048)
    pre_bid_date = models.DateTimeField(null=True, blank=False)
    pre_bid_venue = models.CharField(blank=True, max_length=2048)
    procuring_entity_org_id = models.ForeignKey(Organization, to_field='org_id', related_name='procuring_bid_information', null=True)
    procuring_entity_org = models.CharField(blank=True, max_length=2048)
    client_agency_org_id = models.ForeignKey(Organization, to_field='org_id', related_name='client_bid_information', null=True)
    client_agency_org = models.CharField(blank=True, max_length=2048)
    contact_person = models.CharField(blank=True, max_length=2048)
    contact_person_address = models.TextField(blank=True)
    tender_title = models.CharField(blank=True, max_length=2048)
    description = models.TextField(blank=True)
    other_info = models.TextField(blank=True)
    tender_status = models.CharField(blank=True, max_length=2048)
    reason = models.TextField(blank=True)
    date_available = models.DateTimeField(null=True, blank=True)
    collection_contact = models.CharField(blank=True, max_length=2048)
    collection_point = models.CharField(blank=True, max_length=2048)
    special_instruction = models.TextField(blank=True)
    created_by = models.CharField(max_length=2048)
    creation_date = models.DateTimeField(null=True)
    modified_date = models.DateTimeField(null=True)

    objects = BidInformationManager()

    def __unicode__(self):
        return "{}: {} {}".format(self.ref_id, self.notice_type, self.business_category)


class BidLineItem(models.Model, SelfAwareModelMixin):
    ref_id = models.ForeignKey(BidInformation, to_field='ref_id', null=True)
    line_item_id = models.PositiveIntegerField(unique=True, null=True)
    item_name = models.CharField(max_length=2048, blank=True, null=True)
    item_description = models.TextField(blank=True, null=True)
    qty = models.PositiveIntegerField(null=True)
    uomid = models.PositiveIntegerField(null=True)
    uom = models.CharField(max_length=2048, blank=True, null=True)
    budget = models.FloatField(null=True)
    modified_date = models.DateTimeField(null=True)

    objects = BidLineItemManager()

    def __unicode__(self):
        return "{}:{}".format(self.line_item_id, self.item_name)


class Awards(models.Model, SelfAwareModelMixin):
    award_id = models.PositiveIntegerField(null=False, unique=True)
    ref_id = models.ForeignKey(BidInformation, to_field='ref_id', null=True)
    award_title = models.CharField(max_length=2048, blank=True)
    publish_date = models.DateTimeField(null=True)
    previous_award_id = models.PositiveIntegerField(null=True)
    line_item_id = models.ForeignKey(BidLineItem, to_field='line_item_id', null=True)
    item_name = models.CharField(max_length=2048, blank=True)
    item_description = models.TextField()
    quantity = models.PositiveIntegerField(null=True)
    uom = models.CharField(max_length=2048, blank=True)
    budget = models.FloatField()
    unspc_code = models.CharField(max_length=2048, blank=True)
    unspc_description = models.TextField()
    awardee_id = models.ForeignKey(Organization, to_field='org_id', null=True)
    awardee = models.CharField(max_length=2048, blank=True)
    award_type = models.CharField(max_length=2048, blank=True)
    contract_amt = models.FloatField()
    award_date = models.DateTimeField(null=True)
    award_reason = models.CharField(max_length=2048, blank=True)
    contract_no = models.CharField(max_length=2048, blank=True)
    proceed_date = models.DateTimeField(null=True)
    contract_start_date = models.DateTimeField(null=True)
    contract_end_date = models.DateTimeField(null=True)
    is_short_list = models.IntegerField(null=True)
    is_re_award = models.IntegerField(null=True)
    is_amp = models.IntegerField(null=True)

    master_item = models.ForeignKey('masteritems.MasterItem', related_name='awards_set', blank=True, null=True)

    objects = AwardsManager()

    def __unicode__(self):
     return "{}:{}".format(self.award_id, self.item_name)

    def _get_unit_price(self):
        if self.quantity:
            return self.contract_amt / self.quantity
        else:
            return self.contract_amt
    unit_price = property(_get_unit_price)


class BiddersList(models.Model, SelfAwareModelMixin):
    award_id = models.ForeignKey(Awards, to_field='award_id', null=True)
    line_item_id = models.ForeignKey(BidLineItem, to_field='line_item_id', null=True)
    org_id = models.ForeignKey(Organization, to_field='org_id', null=True)
    bidder_name = models.CharField(max_length=2048)
    modified_date = models.DateTimeField(null=True)

    objects = BiddersListManager()


class ResourceAPIMap(models.Model, SelfAwareModelMixin):
    source_model = models.OneToOneField(ContentType, null=False)
    api_endpoint = models.URLField(null=False)

    def __unicode__(self):
        return '{}: {}'.format(self.source_model, self.api_endpoint)
