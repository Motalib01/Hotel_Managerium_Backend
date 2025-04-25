from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'rating', 'created_at')
    search_fields = ('user__username', 'hotel__name')
    list_filter = ('rating', 'created_at')
