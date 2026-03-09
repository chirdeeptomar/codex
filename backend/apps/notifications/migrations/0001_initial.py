from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [("reports", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="ComplaintExport",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("export_type", models.CharField(default="pdf_bundle", max_length=50)),
                ("file_path", models.CharField(max_length=500)),
                ("status", models.CharField(default="queued", max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("report", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="exports", to="reports.report")),
            ],
        )
    ]
