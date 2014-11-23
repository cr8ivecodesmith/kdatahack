from django.db import models


class MasterItem(models.Model):
    item_name = models.CharField(max_length=2048, blank=True)
    item_description = models.TextField(blank=True)
    uom = models.CharField(max_length=2048, blank=True)

    def __unicode__(self):
        return self.item_name

    def _get_market_price(self):
        market_price = None
        org_prices = self._get_org_prices()
        for id, data in org_prices.items():
            if not market_price:
                market_price = data['price']
            elif data['price'] < market_price:
                market_price = data['price']
        return market_price
    market_price = property(_get_market_price)

    def _get_org_prices(self):
        item_set = self.awards_set.all().order_by('award_date')
        org_prices = {item.awardee_id.org_id: {
            'price': item.unit_price,
            'date': item.award_date,
            'org_name': item.awardee_id.org_name} for item in item_set.iterator()}
        return org_prices

    def _get_price_history(self):
        item_set = self.awards_set.all().order_by('award_date')
        org_prices = dict()
        for item in item_set.iterator():
            if item.awardee_id.org_id not in org_prices:
                org_prices[item.awardee_id.org_id] = list()
            org_prices[item.awardee_id.org_id].append({
                'price': item.unit_price,
                'date': item.award_date,
                'org_name': item.awardee_id.org_name
            })
        return org_prices
    price_history = property(_get_price_history)

    def _get_minmax_price(self):
        min_price = max_price = 0
        for oid, odata in self._get_org_prices().items():
            if odata['price'] > max_price:
                max_price = odata['price']
            if not min_price or odata['price'] < min_price:
                min_price = odata['price']
        return {'min_price': min_price, 'max_price': max_price}
    minmax = property(_get_minmax_price)

