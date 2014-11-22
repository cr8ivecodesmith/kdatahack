from django.db import models


class MasterItem(models.Model):
    item_name = models.CharField(max_length=2048, blank=True)
    uom = models.CharField(max_length=2048, blank=True)

    def __unicode__(self):
        return self.item_name

    @property
    def market_price(self):
        return self._get_market_price()

    def _get_market_price(self):
        # TODO
        item_set = self.bidlineitem_set.all()
        return 0

