from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import apps.reports.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tracking_id", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("tracking_token", models.CharField(default=apps.reports.models.generate_tracking_token, editable=False, max_length=64)),
                ("contact_name", models.CharField(blank=True, max_length=255)),
                ("contact_email", models.EmailField(blank=True, max_length=254)),
                ("category", models.CharField(max_length=120)),
                ("department", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("narrative", models.TextField()),
                ("amount", models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ("anonymity_mode", models.CharField(choices=[("anonymous", "Anonymous"), ("identified", "Identified")], max_length=16)),
                ("status", models.CharField(choices=[("submitted", "Submitted"), ("in_review", "In Review"), ("actioned", "Actioned"), ("rejected", "Rejected")], default="submitted", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("reporter", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="reports", to=settings.AUTH_USER_MODEL)),
            ],
        )
    ]
