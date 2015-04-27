from django.db import models
from importlib import import_module
from datetime import datetime

from core.utils import CSVData

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


class BiddersListManager(models.Manager):

    def import_csv(self, csvfile):
        f = open(csvfile, 'r')
        csv_data = CSVData(f)

        for item in csv_data.items:
            rec = { i.column: i.value for i in item }
            if '_id' in rec.keys():
                del rec['_id']
            data = load_class('philgeps.models.BiddersList')()
            try:
                data.award_id = Awards.objects.get(award_id=rec.get('award_id'))
            except:
                pass

            try:
                data.line_item_id = BidLineItem.objects.get(line_item_id=rec.get('line_item_id'))
            except:
                pass

            try:
                data.org_id = Organization.objects.get(org_id=rec.get('org_id'))
            except:
                pass

            data.bidder_name = rec.get('bidder_name')
            if rec.get('modified_date', ''):
                data.modified_date = datetime.strptime(rec.get('modified_date'), '%Y-%m-%dT%H:%M:%S')
            else:
                data.modified_date = None

            try:
                data.save()
            except Exception as e:
                pdb.set_trace()
                pass


class AwardsManager(models.Manager):

    def import_csv(self, csvfile):
        f = open(csvfile, 'r')
        csv_data = CSVData(f)

        for item in csv_data.items:
            rec = { i.column: i.value for i in item }
            if '_id' in rec.keys():
                del rec['_id']
            data = load_class('philgeps.models.Awards')()
            data.award_id = rec.get('award_id')
            try:
                data.ref_id = BidInformation.objects.get(ref_id=rec.get('ref_id'))
            except:
                pass
            data.award_title = rec.get('award_title')
            data.reason = rec.get('reason')
            data.award_status = rec.get('award_status')
            if rec.get('publish_date', ''):
                publish_date = datetime.strptime(rec.get('publish_date'), '%Y-%m-%dT%H:%M:%S')
            else:
                publish_date = None
            data.previous_award_id = rec.get('previous_award_id')
            try:
                data.line_item_id = BidLineItem.objects.get(line_item_id=rec.get('line_item_id'))
            except:
                pass
            data.item_name = rec.get('item_name')
            data.item_description = rec.get('item_description')
            data.qty = rec.get('qty')
            data.uom = rec.get('uom')
            data.unspsc_code = rec.get('unspsc_code')
            data.unspsc_description = rec.get('unspsc_description')
            data.budget = rec.get('budget')

            try:
                data.awardee_id = Organization.objects.get(org_id=rec.get('awardee_id'))
            except Exception as e:
                pass

            data.awardee = rec.get('awardee')
            data.award_type = rec.get('award_type')
            data.contract_amt = rec.get('contract_amt')
            if rec.get('award_date', ''):
                award_date = datetime.strptime(rec.get('award_date'), '%Y-%m-%dT%H:%M:%S')
            else:
                award_date = None
            data.award_reason = rec.get('award_reason')
            data.contract_no = rec.get('contract_no')

            if rec.get('proceed_date', ''):
                data.proceed_date = datetime.strptime(rec.get('proceed_date'), '%Y-%m-%dT%H:%M:%S')
            else:
                data.proceed_date = None

            if rec.get('contract_start_date', ''):
                contract_start_date = datetime.strptime(rec.get('contract_start_date'), '%Y-%m-%dT%H:%M:%S')
            else:
                contract_start_date = None

            if rec.get('contract_enddate', ''):
                contract_end_date = datetime.strptime(rec.get('contract_enddate'), '%Y-%m-%dT%H:%M:%S')
            else:
                contract_end_date = None

            if rec.get('is_short_list') == 'False':
                data.is_short_list = False
            elif rec.get('is_short_list') == 'True':
                data.is_short_list = True
            else: 
                data.is_short_list = None

            if rec.get('is_reaward') == 'False':
                data.is_reaward = False
            elif rec.get('is_reaward') == 'True':
                data.is_reaward = True
            else: 
                data.is_reaward = None

            if rec.get('is_amp') == 'False':
                data.is_amp = False
            elif rec.get('is_amp') == 'True':
                data.is_amp = True
            else: 
                data.is_amp = None

            if rec.get('modified_date', ''):
                data.modified_date = datetime.strptime(rec.get('modified_date'), '%Y-%m-%dT%H:%M:%S')
            else:
                data.modified_date = None

            try:
                data.save()
            except Exception as e:
                pdb.set_trace()
                pass