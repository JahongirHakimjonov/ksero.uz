from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from apps.backend.models.station import Station, StationCredential


class StationCredentialInline(StackedInline):
    model = StationCredential
    extra = 1
    tab = True


@admin.register(Station)
class StationAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "longitude",
        "latitude",
        "address",
        "paper_count",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "address")
    list_filter = ("is_active",)
    inlines = (StationCredentialInline,)


@admin.register(StationCredential)
class StationCredentialAdmin(ModelAdmin):
    list_display = (
        "id",
        "station",
        "auth_uri",
        "client_id",
        "secret",
        "device",
        "host",
        "password",
        "created_at",
        "updated_at",
    )
    search_fields = ("station__name", "auth_uri", "client_id", "device", "host")
    list_filter = ("station",)
    autocomplete_fields = ("station",)
