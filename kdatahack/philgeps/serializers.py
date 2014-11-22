from rest_framework import serializers

from .models import (
    BiddersList,
    Awards,
    Organization,
    BidLineItem,
    BidInformation,
)


class BiddersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiddersList


class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization


class BidLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidLineItem


class BidInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidInformation
