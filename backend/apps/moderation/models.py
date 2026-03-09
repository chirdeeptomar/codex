from django.conf import settings
from django.db import models
from apps.reports.models import Report


class ModerationAction(models.Model):
    report = models.ForeignKey(Report, related_name="moderation_actions", on_delete=models.CASCADE)
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    action = models.CharField(max_length=120)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.action} on {self.report_id}"
