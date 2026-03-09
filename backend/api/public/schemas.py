from ninja import Schema


class AnalyticsSummaryOut(Schema):
    total_reports: int
    anonymous_reports: int
    identified_reports: int


class HotspotOut(Schema):
    location: str
    count: int
