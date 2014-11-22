from django.db import models


# Create your models here.
class BiddersList(models.Model):
	award_id = models.ForeignKey('Awards', to_field='award_id')
	line_item_id = models.ForeignKey('BidLineItem', to_field='line_item_id')
	org_id = models.ForeignKey('Organization', to_field='org_id')
	bidder_name = models.CharField()
 

class Awards(models.Models):
	award_id = models.PositiveIntegerField(null=False)
	ref_id = models.ForeignKey('BidInformation', to_field='ref_id')
	award_title = models.CharField()
	publish_date = models.DateTimeField()
	previous_award_id = models.PositiveIntegerField(null=True)
	line_item_id = models.ForeignKey('BidLineItem', to_field='line_item_id')
	item_name = models.CharField()
	item_description = models.TextField()
	quantity = models.PositiveIntegerField(null=True)
	uom = models.CharField()
	budget = models.FloatField()
	unspc_code = models.CharField()
	unspc_description = models.TextField()
	awardee_id = models.ForeignKey('Organization', to_field='org_id')
	awardee = models.CharField()
	award_type = models.CharField()
	contract_amt = models.FloatField()
	award_date = models.DateTimeField(blank=True)
	award_reason = models.CharField()
	contract_no = models.CharField()
	proceed_date = models.DateTimeField(blank=True)
	contract_start_date = models.DateTimeField(blank=True)
	contract_end_date = models.DateTimeField(blank=True)
	is_short_list = models.IntegerField(maxlength=1)
	is_re_award = models.IntegerField(maxlength=1)
	is_amp = models.IntegerField(maxlength=1)