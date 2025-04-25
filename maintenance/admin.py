from django.contrib import admin
from .models import MaintenanceRequest

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('room', 'issue', 'reported_at', 'status')
    search_fields = ('room__name', 'issue')
    list_filter = ('status', 'reported_at')
