from django.db import models


class MasterItem(models.Model):
    item_name = models.CharField(max_length=2048, blank=True)
    item_description = models.TextField(blank=True)
    uom = models.CharField(max_length=2048, blank=True)

    def __unicode__(self):
        return self.item_name

    def _get_market_price(self):
        market_price = None
        org_prices = self._get_price_history()
        for id, data in org_prices.items():
            if not market_price:
                market_price = data['price']
            elif data['price'] < market_price:
                market_price = data['price']
        return market_price
    market_price = property(_get_market_price)

    def _get_price_history(self):
        item_set = self.awards_set.all()
        org_prices = {item.awardee_id.org_id: {
            'price': item.unit_price,
            'date': item.award_date,
            'org_name': item.awardee} for item in item_set.iterator()}
        return org_prices

