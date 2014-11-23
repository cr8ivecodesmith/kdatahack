from rest_framework import serializers

from .models import MasterItem


class MasterItemSerializer(serializers.ModelSerializer):
    market_price = serializers.Field(source='_get_market_price')
    class Meta:
        model = MasterItem
        fields = (
            'id',
            'item_name',
            'item_description',
            'uom',
            'market_price',
        )
