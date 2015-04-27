import re
from optparse import make_option
from django.core.management.base import BaseCommand
import pdb
import philgeps
import os
# from importlib import import_module
# from datetime import datetime

# from messytables import (CSVTableSet, headers_guess, headers_processor, offset_processor,
#                          type_guess, types_processor)

from philgeps.models import BidInformation, BidLineItem, Organization, Awards, BiddersList
# def load_class(full_class_path):
#     """Dynamically load a class from a string

#         Args:
#             full_class_path (string) - Full path of the class to load
#                                        i.e. app.views.CustomView

#     """
#     path_data = full_class_path.split('.')
#     module_path = '.'.join(path_data[:-1])
#     class_name = path_data[-1]

#     try:
#         module = import_module(module_path)
#         return getattr(module, class_name)
#     except ImportError as e:
#         raise e

class Command(BaseCommand):
    option_list = (
        make_option(
            '--model',
            action='store',
            dest='model',
            type='string',
            default='',
            help="""
Specify staging models to operate on. i.e. --model BidLineItem
            """,
        ),
        make_option(
            '--csvfile',
            action='store',
            dest='csvfile',
            type='string',
            default='',
            help="""
Specify staging filename/fullpath of CSV to operate on. i.e. --csvfile spambaconeggs.csv OR /home/monty/spambaconeggs.csv
            """,
        ),
    ) + BaseCommand.option_list

    def handle(self, *args, **options):
        model = []
        if options['model'].strip():
            model = re.sub(r'\s', '', options['model'])
            if model not in dir(philgeps.models):
                print "Model is invalid!"
                return
        if options['csvfile'].strip():
            csvfile = re.sub(r'\s', '', options['csvfile'])
            if not os.path.exists(csvfile):
                print "CSV file does not exist!"
                return

        f = open(csvfile, 'r')
        #csv_data = CSVData(f)

        if model == 'BiddersList':
            #create_bidder_list_records(csv_data.items)
            BiddersList.objects.import_csv(csvfile)
        elif model == 'Awards':
            #create_awards_records(csv_data.items)
            Awards.objects.import_csv(csvfile)
        elif model == 'Organization':
            create_organization_records(csv_data.items)
        elif model == 'BidLineItem':
            create_bid_line_item_records(csv_data.items)
        elif model == 'BidInformation':
            create_bid_information_records(csv_data.items)


def create_organization_records(items):
    for item in items:
        rec = { i.column: i.value for i in item }
        if '_id' in rec.keys():
            del rec['_id']
        data = load_class('philgeps.models.Organization')()
        data.org_id = rec.get('org_id')
        data.member_type_id = rec.get('member_type_id')
        data.member_type = rec.get('member_type')
        data.parent_org_id = rec.get('parent_org_id')
        data.is_org_foreign = rec.get('is_org_foreign')
        data.org_name = rec.get('org_name')
        data.goverment_branch = rec.get('goverment_branch')
        data.government_organization_type = rec.get('government_organization_type')
        data.supplier_form_of_organization = rec.get('supplier_form_of_organization')
        data.supplier_organization_type = rec.get('supplier_organization_type')
        if rec.get('org_reg_date', ''):
            data.org_reg_date = datetime.strptime(rec.get('org_reg_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.org_reg_date = None
        data.website = rec.get('website')
        data.org_description = rec.get('org_description')
        data.country_code = rec.get('country_code')
        data.country = rec.get('country')
        data.region = rec.get('region')
        data.province = rec.get('province')
        data.city = rec.get('city')
        data.address1 = rec.get('address1')
        data.address2 = rec.get('address2')
        data.address3 = rec.get('address3')
        data.zip_code = rec.get('zip_code')
        data.org_status = rec.get('org_status')
        if rec.get('modified_date', ''):
            data.modified_date = datetime.strptime(rec.get('modified_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.modified_date = None

        try:
            data.save()
        except Exception as e:
            pdb.set_trace()
            pass

def create_bid_line_item_records(items):
    for item in items:
        rec = { i.column: i.value for i in item }
        if '_id' in rec.keys():
            del rec['_id']
        data = load_class('philgeps.models.BidLineItem')()

        try:
            data.award_id = Awards.objects.get(ref_id=rec.get('ref_id'))
        except:
            pass

        try:
            data.line_item_id = BidInformation.objects.get(line_item_id=rec.get('line_item_id'))
        except:
            pass

        data.item_name = rec.get('item_name')
        data.item_description = rec.get('item_description')
        data.qty = rec.get('qty')
        data.uomid = rec.get('uomid')
        data.uom = rec.get('uom')

        if rec.get('modified_date', ''):
            data.modified_date = datetime.strptime(rec.get('modified_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.modified_date = None

        try:
            data.save()
        except Exception as e:
            pdb.set_trace()
            pass

def create_bid_information_records(items):
    for item in items:
        rec = { i.column: i.value for i in item }
        if '_id' in rec.keys():
            del rec['_id']

        data = load_class('philgeps.models.BidInformation')()

        try:
            data.ref_id = int(rec.get('ref_id'))
        except:
            continue

        data.ref_no = rec.get('ref_no')
        data.stage = rec.get('stage')
        data.stage2_ref_id = rec.get('stage2_ref_id')

        try:
            data.org_id = Organization.objects.get(org_id=rec.get('org_id'))
        except:
            pass

        data.classification = rec.get('classification')
        data.solicitation_no = rec.get('solicitation_no')
        data.notice_type = rec.get('notice_type')
        data.business_category = rec.get('business_category')
        data.procurement_mode = rec.get('procurement_mode')
        data.funding_instrument = rec.get('funding_instrument')
        data.funding_source = rec.get('funding_source')
        data.approved_budget = rec.get('approved_budget')

        if rec.get('publish_date', ''):
            data.publish_date = datetime.strptime(rec.get('publish_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.publish_date = None

        if rec.get('closing_date', ''):
            data.closing_date = datetime.strptime(rec.get('closing_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.closing_date = None

        data.contract_duration = rec.get('contract_duration')
        data.calendar_type = rec.get('calendar_type')
        data.trade_agreement = rec.get('trade_agreement')

        if rec.get('pre_bid_date', ''):
            data.pre_bid_date = datetime.strptime(rec.get('pre_bid_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.pre_bid_date = None

        data.pre_bid_venue = rec.get('pre_bid_venue')

        try:
            data.procuring_entity_org_id = Organization.objects.get(procuring_entity_org_id=rec.get('procuring_entity_org_id'))
        except:
            pass

        data.procuring_entity_org = rec.get('procuring_entity_org')

        try:
            data.client_agency_org_id = Organization.objects.get(client_agency_org_id=rec.get('client_agency_org_id'))
        except:
            pass

        data.client_agency_org = rec.get('procuring_entity_org')
        data.contact_person = rec.get('contact_person')
        data.contact_person_address = rec.get('contact_person_address')
        data.tender_title = rec.get('tender_title')
        data.description = rec.get('description')
        data.other_info = rec.get('other_info')
        data.tender_status = rec.get('tender_status')
        data.reason = rec.get('reason')

        if rec.get('date_available', ''):
            data.date_available = datetime.strptime(rec.get('date_available'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.date_available = None

        data.collection_contact = rec.get('collection_contact')
        data.collection_point = rec.get('collection_point')
        data.special_instruction = rec.get('special_instruction')
        data.created_by = rec.get('created_by')

        if rec.get('created_date', ''):
            data.created_date = datetime.strptime(rec.get('created_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.created_date = None

        if rec.get('modified_date', ''):
            data.modified_date = datetime.strptime(rec.get('modified_date'), '%Y-%m-%dT%H:%M:%S')
        else:
            data.modified_date = None

        try:
            data.save()
        except Exception as e:
            pdb.set_trace()
            pass