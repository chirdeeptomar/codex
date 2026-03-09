# Corruption Transparency Platform (India) — MVP Scaffold

This repository contains an MVP monolith backend + React frontend scaffold for a corruption transparency platform.

## Stack

- **Backend**: Django 6.0.3, Django Ninja, PostgreSQL, Celery, Redis
- **Frontend**: React + Vite + React Router + TanStack Query
- **Storage**: S3-compatible private evidence storage abstraction (MinIO in local dev)
- **Runtime**: ASGI via Uvicorn
- **Local Dev**: Docker Compose

## Architecture

- Monolith backend with app modules:
  - `apps.accounts`
  - `apps.reports`
  - `apps.evidence`
  - `apps.moderation`
  - `apps.routing`
  - `apps.analytics`
  - `apps.audits`
  - `apps.notifications`
- API routers:
  - `api.public`
  - `api.citizen`
  - `api.moderator`
- Django Admin is used for moderator/admin workflows.
- Evidence is private-by-default using an S3 storage backend with private ACLs.

## MVP Features Included

1. Citizen report submission with anonymity mode.
2. Anonymous tracking flow via `tracking_id` + secret `tracking_token`.
3. Evidence metadata + file object registration.
4. Moderator/admin visibility through Django admin registrations.
5. Complaint export model + placeholder export service.
6. Public aggregated analytics endpoints only.
7. Audit event model + logging service for sensitive actions.

## API Endpoints

- `POST /api/citizen/reports`
- `GET /api/citizen/reports/{tracking_id}?token=...`
- `POST /api/citizen/reports/{tracking_id}/attachments?token=...`
- `GET /api/public/analytics/summary`
- `GET /api/public/analytics/hotspots`

## Local setup

1. Copy env file:

   ```bash
   cp .env.example .env
   ```

2. Start services:

   ```bash
   docker compose up --build
   ```

3. Backend will be available at:
   - API: `http://localhost:8000/api/`
   - Admin: `http://localhost:8000/admin/`

4. Frontend will be available at:
   - `http://localhost:5173`

## Developer Notes

- Django settings split:
  - `config/settings/base.py`
  - `config/settings/dev.py`
- Celery app: `config/celery.py`
- Private evidence storage abstraction: `apps/evidence/storage.py`
- Service placeholders:
  - PDF/export queue: `apps/reports/services.py`
  - Notifications: `apps/notifications/services.py`

## Running tests locally

```bash
cd backend
pytest
```
