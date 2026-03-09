from django.contrib import admin
from .models import EvidenceFile


@admin.register(EvidenceFile)
class EvidenceFileAdmin(admin.ModelAdmin):
    list_display = ("id", "report", "original_filename", "mime_type", "size", "created_at")
    readonly_fields = ("sha256_hash", "created_at")
    search_fields = ("report__tracking_id", "original_filename")
