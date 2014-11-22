from rest_framework import serializers

from .models import MasterItem


class MasterItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterItem
