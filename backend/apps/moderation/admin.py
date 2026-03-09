from django.contrib import admin
from .models import ModerationAction


@admin.register(ModerationAction)
class ModerationActionAdmin(admin.ModelAdmin):
    list_display = ("report", "moderator", "action", "created_at")
    search_fields = ("report__tracking_id", "moderator__username", "action")
