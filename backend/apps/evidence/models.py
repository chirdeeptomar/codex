from django.db import models
from apps.reports.models import Report
from .storage import PrivateEvidenceStorage


class EvidenceFile(models.Model):
    report = models.ForeignKey(Report, related_name="evidence_files", on_delete=models.CASCADE)
    file = models.FileField(upload_to="evidence/%Y/%m/%d", storage=PrivateEvidenceStorage())
    original_filename = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=120)
    size = models.BigIntegerField()
    sha256_hash = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.original_filename} ({self.report_id})"
