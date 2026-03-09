from django.contrib import admin
from .models import ComplaintExport


@admin.register(ComplaintExport)
class ComplaintExportAdmin(admin.ModelAdmin):
    list_display = ("report", "export_type", "status", "created_at")
    search_fields = ("report__tracking_id", "status")
