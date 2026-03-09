import pytest
from ninja.testing import TestClient

from config.urls import api
from apps.reports.models import Report


pytestmark = pytest.mark.django_db
client = TestClient(api)


def test_create_report_returns_tracking_token():
    payload = {
        "category": "bribery",
        "department": "Municipal Office",
        "location": "Delhi",
        "narrative": "Asked to pay unofficial fee",
        "amount": "5000.00",
        "anonymity_mode": "anonymous",
    }

    response = client.post("/citizen/reports", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["tracking_id"]
    assert body["tracking_token"]
    assert Report.objects.count() == 1


def test_public_analytics_summary_aggregates_counts():
    Report.objects.create(
        category="fraud",
        department="PDS",
        location="Mumbai",
        narrative="Diversion",
        anonymity_mode=Report.AnonymityMode.ANONYMOUS,
    )
    Report.objects.create(
        category="fraud",
        department="PDS",
        location="Mumbai",
        narrative="Demanded bribe",
        anonymity_mode=Report.AnonymityMode.IDENTIFIED,
    )

    response = client.get("/public/analytics/summary")

    assert response.status_code == 200
    assert response.json() == {
        "total_reports": 2,
        "anonymous_reports": 1,
        "identified_reports": 1,
    }
