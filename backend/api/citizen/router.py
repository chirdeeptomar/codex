from uuid import UUID
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from ninja import Router

from apps.audits.services import log_event
from apps.evidence.models import EvidenceFile
from apps.notifications.services import NotificationService
from apps.reports.models import Report
from apps.reports.services import ComplaintExportService
from .schemas import AttachmentIn, AttachmentOut, ReportCreateIn, ReportCreateOut, ReportDetailOut

router = Router(tags=["citizen"])


@router.post("/reports", response=ReportCreateOut)
async def create_report(request, payload: ReportCreateIn):
    report = Report.objects.create(
        category=payload.category,
        department=payload.department,
        location=payload.location,
        narrative=payload.narrative,
        amount=payload.amount,
        anonymity_mode=payload.anonymity_mode,
        contact_name=payload.contact_name or "",
        contact_email=payload.contact_email or "",
    )
    ComplaintExportService.queue_pdf_export(report)
    NotificationService.notify_report_created(report)
    log_event(request, "report.created", "report", str(report.tracking_id))
    return ReportCreateOut(
        tracking_id=report.tracking_id,
        tracking_token=report.tracking_token,
        status=report.status,
    )


@router.get("/reports/{tracking_id}", response=ReportDetailOut)
def get_report(request, tracking_id: UUID, token: str):
    report = get_object_or_404(Report, tracking_id=tracking_id, tracking_token=token)
    log_event(request, "report.viewed", "report", str(report.tracking_id))
    return report


@router.post("/reports/{tracking_id}/attachments", response=AttachmentOut)
def add_attachment(request, tracking_id: UUID, token: str, payload: AttachmentIn):
    report = get_object_or_404(Report, tracking_id=tracking_id, tracking_token=token)
    evidence = EvidenceFile.objects.create(
        report=report,
        original_filename=payload.original_filename,
        mime_type=payload.mime_type,
        size=payload.size,
        sha256_hash=payload.sha256_hash,
    )
    evidence.file.save(payload.storage_key, ContentFile(b""), save=True)
    log_event(request, "evidence.added", "evidence", str(evidence.id), {"report_id": str(report.tracking_id)})
    return evidence
