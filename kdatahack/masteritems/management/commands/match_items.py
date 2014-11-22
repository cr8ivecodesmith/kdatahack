from django.core.management.base import BaseCommand
from masteritems.models import MasterItem
from philgeps.models import Awards


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for award in Awards.objects.filter(master_item__isnull=True).iterator():
            if MasterItem.objects.filter(
                item_name__iexact=award.item_name, uom=award.uom).exists():
                master_item = MasterItem.objects.get(item_name__iexact=award.items, uom=award.uom)
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
                
