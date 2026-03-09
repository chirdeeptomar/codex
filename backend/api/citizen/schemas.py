from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID
from ninja import Schema


class ReportCreateIn(Schema):
    category: str
    department: str
    location: str
    narrative: str
    amount: Optional[Decimal] = None
    anonymity_mode: str
    contact_name: Optional[str] = None
    contact_email: Optional[str] = None


class ReportCreateOut(Schema):
    tracking_id: UUID
    tracking_token: str
    status: str


class ReportDetailOut(Schema):
    tracking_id: UUID
    category: str
    department: str
    location: str
    narrative: str
    amount: Optional[Decimal]
    anonymity_mode: str
    status: str
    created_at: datetime


class AttachmentIn(Schema):
    original_filename: str
    mime_type: str
    size: int
    sha256_hash: str
    storage_key: str


class AttachmentOut(Schema):
    id: int
    original_filename: str
    mime_type: str
    size: int
    created_at: datetime
