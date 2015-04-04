from django.contrib import admin

from . import models


@admin.register(models.BiddersList)
class BiddersListAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Awards)
class AwardsItemAdmin(admin.ModelAdmin):
    search_fields = ['item_name', 'item_description']

@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.BidLineItem)
class BidLineItemAdmin(admin.ModelAdmin):
    search_fields = ['item_name']

@admin.register(models.BidInformation)
class BidInformationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ResourceAPIMap)
class ResourceAPIMapAdmin(admin.ModelAdmin):
    pass
