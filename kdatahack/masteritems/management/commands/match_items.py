from django.core.management.base import BaseCommand
from masteritems.models import MasterItem
from philgeps.models import Awards, Organization

from random import randrange

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for award in Awards.objects.exclude(item_name='').iterator():
            randid = randrange(10)+1
            org = Organization.objects.get(pk=randid)
            award.awardee_id = org
            if MasterItem.objects.filter(
                item_name__iexact=award.item_name).exists():
                master_item = MasterItem.objects.get(item_name__iexact=award.item_name)
                award.master_item = master_item
                print "{} <- {}".format(master_item.item_name, award.item_name)
                award.save()
            else:
                master_item = MasterItem(
                    item_name=award.item_name,
                    item_description=award.item_description,
                    uom=award.uom)
                print "Creating Master Item: {}".format(master_item.item_name)
                master_item.save()
                award.master_item = master_item
                print "{} <- {}".format(master_item.item_name, award.item_name)
                award.save()
                
