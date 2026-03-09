from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

from api.citizen.router import router as citizen_router
from api.moderator.router import router as moderator_router
from api.public.router import router as public_router

api = NinjaAPI(title="Corruption Transparency API", version="0.1.0")
api.add_router("/citizen/", citizen_router)
api.add_router("/public/", public_router)
api.add_router("/moderator/", moderator_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", include("apps.analytics.urls")),
]
