import re
from optparse import make_option
from django.core.management.base import BaseCommand
import pdb
import philgeps
import os
from importlib import import_module
from datetime import datetime

from messytables import (CSVTableSet, headers_guess, headers_processor, offset_processor,
                         type_guess, types_processor)

def load_class(full_class_path):
    """Dynamically load a class from a string

        Args:
            full_class_path (string) - Full path of the class to load
                                       i.e. app.views.CustomView

    """
    path_data = full_class_path.split('.')
    module_path = '.'.join(path_data[:-1])
    class_name = path_data[-1]

    try:
        module = import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        raise e

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
        csv_data = CSVData(f)

        if model == 'BiddersList':
            create_bidder_list_records(csv_data.items)
        elif model == 'Awards':
            create_awards_records(csv_data.items)
        elif model == 'Organization':
            create_organization_records(csv_data.items)
        elif model == 'BidLineItem':
            create_bid_line_item_records(csv_data.items)
        elif model == 'BidInformation':
            create_bid_information_records(csv_data.items)

class CSVData(object):

    def __init__(self, file_object, headers=None, offset=None, types=None):
        table_set = CSVTableSet(file_object)
        self._row_set = table_set.tables[0]

        self.headers = self.set_headers(headers)
        self.offset = self.set_offset(offset)
        self.types = self.set_types(types)

        self._row_set.register_processor(headers_processor(self.headers))
        self._row_set.register_processor(offset_processor(self.offset))
        self._row_set.register_processor(types_processor(self.types))

        self.items = self._row_set

    def set_headers(self, headers=None):
        if not headers:
            headers = headers_guess(self._row_set.sample)[1]
        return headers

    def set_offset(self, offset=None):
        if not offset:
            offset = headers_guess(self._row_set.sample)[0] + 1
        return offset

    def set_types(self, types=None):
        if not types:
            types = type_guess(self._row_set.sample, strict=True)
        return types


def create_bidder_list_records(items):
    pass

def create_awards_records(items):
    pass

def create_organization_records(items):
    for item in items:
        rec = { i.column: i.value for i in item }
        if '_id' in rec.keys():
            del rec['_id']
        try:
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
            data.save()
        except Exception as e:
            pdb.set_trace()
            pass

def create_bid_line_item_records(items):
    pass

def create_bid_information_records(item):
    pass