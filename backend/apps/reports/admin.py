from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("tracking_id", "category", "department", "anonymity_mode", "status", "created_at")
    list_filter = ("status", "anonymity_mode", "category")
    search_fields = ("tracking_id", "department", "location")
    readonly_fields = ("tracking_id", "tracking_token", "created_at", "updated_at")
