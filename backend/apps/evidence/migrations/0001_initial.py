from django.db import migrations, models
import django.db.models.deletion
import apps.evidence.storage


class Migration(migrations.Migration):
    initial = True

    dependencies = [("reports", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="EvidenceFile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file", models.FileField(storage=apps.evidence.storage.PrivateEvidenceStorage(), upload_to="evidence/%Y/%m/%d")),
                ("original_filename", models.CharField(max_length=255)),
                ("mime_type", models.CharField(max_length=120)),
                ("size", models.BigIntegerField()),
                ("sha256_hash", models.CharField(max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("report", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="evidence_files", to="reports.report")),
            ],
        )
    ]
