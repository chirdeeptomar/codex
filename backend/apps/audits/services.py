from typing import Any
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest

from .models import AuditEvent


def log_event(request: HttpRequest, action: str, target_type: str, target_id: str, metadata: dict[str, Any] | None = None) -> AuditEvent:
    actor = None
    if hasattr(request, "user") and request.user and not isinstance(request.user, AnonymousUser):
        actor = request.user
    return AuditEvent.objects.create(
        actor=actor,
        action=action,
        target_type=target_type,
        target_id=target_id,
        metadata=metadata or {},
    )
