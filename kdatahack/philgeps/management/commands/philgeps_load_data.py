import re
from optparse import make_option
from django.core.management.base import BaseCommand
import pdb
import philgeps
import os

from philgeps.models import BidInformation, BidLineItem, Organization, Awards, BiddersList


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
            #create_organization_records(csv_data.items)
            Organization.objects.import_csv(csvfile)
        elif model == 'BidLineItem':
            #create_bid_line_item_records(csv_data.items)
            BidLineItem.objects.import_csv(csvfile)
        elif model == 'BidInformation':
            #create_bid_information_records(csv_data.items)
            BidInformation.objects.import_csv(csvfile)
