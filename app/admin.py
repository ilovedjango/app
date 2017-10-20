# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


admin.site.site_header = 'Data Base Administration'

from .models import Account, Address, PayDetails, Lead

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark as used"

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'passwd', 'phone',]
    ordering = ['user']
admin.site.register(Account, AccountAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'address2', 'city', 'zip', 'state', 'country',]
admin.site.register(Address, AddressAdmin)


class PayDetailsAdmin(admin.ModelAdmin):
    list_display = ['paynumber', 'expmonth', 'expyear', 'cvv']
admin.site.register(PayDetails, PayDetailsAdmin)

class LeadAdmin(admin.ModelAdmin):
    list_display = ['user', 'passwd', 'phone', 'street', 'address2', 'city', 'zip', 'state', 'country', 'paynumber', 'expmonth', 'expyear', 'cvv']
admin.site.register(Lead, LeadAdmin)
