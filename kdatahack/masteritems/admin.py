from django.contrib import admin

from .models import MasterItem


@admin.register(MasterItem)
class MasterItemAdmin(admin.ModelAdmin):
    pass

