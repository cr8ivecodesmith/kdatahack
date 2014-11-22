from django.db import models


class Organization(models.Model):
    org_id = models.PositiveIntegerField(null=False)
    member_type_id = models.PositiveIntegerField(null=True)
    member_type = models.CharField(blank=True)
    parent_org_id = models.PositiveIntegerField(null=True)
    is_org_foreign = models.NullBooleanField()
    org_name = models.CharField(blank=True)
    goverment_branch = models.CharField(blank=True)
    government_organization_type = models.CharField(blank=True)
    supplier_form_of_organization = models.CharField(blank=True)
    supplier_organization_type = models.CharField(blank=True)
    org_reg_date = models.DateTimeField(blank=True)
    website = models.UrlField(blank=True)
    org_description = models.TextField(blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    country = models.CharField(blank=True)
    region = models.CharField(blank=True)
    province = models.CharField(blank=True)
    city = models.CharField(blank=True)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    address3 = models.TextField(blank=True)
    zip_code = models.PositiveIntegerField(null=True)
    org_status = models.CharField(blank=True)
    modified_date = models.DateTimeField(blank=True)


class BidLineItem(models.Model):
    ref_id = models.ForeignKey('BidInformation', to_field='ref_id')
    line_item_id = models.PositiveIntegerField(null=False)
    item_name = models.CharField(blank=True)
    item_description = models.TextField(blank=True)
    qty = models.PositiveIntegerField(null=True)
    uomid = models.PositiveIntegerField(null=True)
    uom = models.CharField(blank=True)
    budget = models.FloatField(null=True)
    modified_date = models.DateTimeField(blank=True)

