import secrets
import uuid
from django.conf import settings
from django.db import models


def generate_tracking_token() -> str:
    return secrets.token_hex(16)


class Report(models.Model):
    class AnonymityMode(models.TextChoices):
        ANONYMOUS = "anonymous", "Anonymous"
        IDENTIFIED = "identified", "Identified"

    class Status(models.TextChoices):
        SUBMITTED = "submitted", "Submitted"
        IN_REVIEW = "in_review", "In Review"
        ACTIONED = "actioned", "Actioned"
        REJECTED = "rejected", "Rejected"

    tracking_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    tracking_token = models.CharField(max_length=64, default=generate_tracking_token, editable=False)
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reports",
    )
    contact_name = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    category = models.CharField(max_length=120)
    department = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    narrative = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    anonymity_mode = models.CharField(max_length=16, choices=AnonymityMode.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SUBMITTED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.category} ({self.tracking_id})"
