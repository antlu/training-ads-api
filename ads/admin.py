from django.contrib import admin

from ads.forms import AdForm
from ads.models import Advertisement


class AdAdmin(admin.ModelAdmin):
    """Ad customized representation for admin."""

    form = AdForm


admin.site.register(Advertisement, AdAdmin)
