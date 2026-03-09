from django.db.models import Count, Q
from ninja import Router

from apps.reports.models import Report
from .schemas import AnalyticsSummaryOut, HotspotOut

router = Router(tags=["public"])


@router.get("/analytics/summary", response=AnalyticsSummaryOut)
def analytics_summary(request):
    qs = Report.objects.all()
    total = qs.count()
    anonymous = qs.filter(anonymity_mode=Report.AnonymityMode.ANONYMOUS).count()
    identified = qs.filter(anonymity_mode=Report.AnonymityMode.IDENTIFIED).count()
    return AnalyticsSummaryOut(total_reports=total, anonymous_reports=anonymous, identified_reports=identified)


@router.get("/analytics/hotspots", response=list[HotspotOut])
def analytics_hotspots(request):
    data = (
        Report.objects.values("location")
        .annotate(count=Count("id", filter=Q(status__in=[Report.Status.SUBMITTED, Report.Status.IN_REVIEW, Report.Status.ACTIONED])))
        .order_by("-count")[:20]
    )
    return [HotspotOut(location=i["location"], count=i["count"]) for i in data if i["location"]]
