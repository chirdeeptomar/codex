from django.contrib.auth.models import Group


def ensure_default_roles() -> None:
    for role in ("citizen", "moderator", "admin"):
        Group.objects.get_or_create(name=role)
