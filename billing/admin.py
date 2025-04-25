from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'amount', 'status', 'created_at')
    search_fields = ('reservation__user__username', 'reservation__room__name')
    list_filter = ('status', 'created_at')

