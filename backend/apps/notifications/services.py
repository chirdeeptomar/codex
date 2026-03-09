from apps.reports.models import Report


class NotificationService:
    """Placeholder interface for notifications (email/SMS/whatsapp)."""

    @staticmethod
    def notify_report_created(report: Report) -> None:
        # Intentionally no-op for MVP scaffold.
        _ = report
