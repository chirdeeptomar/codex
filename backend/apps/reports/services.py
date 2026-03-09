from pathlib import Path
from apps.notifications.models import ComplaintExport
from apps.reports.models import Report


class ComplaintExportService:
    """Placeholder interface for asynchronous PDF/bundle generation."""

    @staticmethod
    def queue_pdf_export(report: Report) -> ComplaintExport:
        return ComplaintExport.objects.create(
            report=report,
            export_type="pdf_bundle",
            file_path=str(Path("exports") / f"{report.tracking_id}.pdf"),
            status="queued",
        )
