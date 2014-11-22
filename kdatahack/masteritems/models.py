from django.db import models


class MasterItem(models.Model):
    item_name = models.CharField(max_length=2048, blank=True)
    item_description = models.TextField(blank=True)
    uom = models.CharField(max_length=2048, blank=True)

    def __unicode__(self):
        return self.item_name

    def _get_market_price(self):
        org_prices = {}
        item_set = self.awards_set.all()
        for item in item_set.iterator():
            org_id = item.awardee_id.org_id
            if org_id not in org_prices:
                org_prices[org_id] = {
                    'price': item.unit_price,
                    'date': item.award_date,
                    'org_name': item.awardee}
            elif item.unit_price < org_prices[org_id] and item.award_date >= org_prices[org_id]['date']:
                org_price[org_id]['price'] = item.unit_price
        market_price = None
        for id, data in org_prices.items():
            if not market_price:
                market_price = data['price']
            elif data['price'] < market_price:
                market_price = data['price']
        return market_price
    market_price = property(_get_market_price)
