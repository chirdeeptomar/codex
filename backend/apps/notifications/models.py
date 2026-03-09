from django.db import models
from apps.reports.models import Report


class ComplaintExport(models.Model):
    report = models.ForeignKey(Report, related_name="exports", on_delete=models.CASCADE)
    export_type = models.CharField(max_length=50, default="pdf_bundle")
    file_path = models.CharField(max_length=500)
    status = models.CharField(max_length=50, default="queued")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.report_id}:{self.export_type}:{self.status}"
