from django.contrib import admin

from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at')