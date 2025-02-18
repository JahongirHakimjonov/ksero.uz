from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.ads import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(SortableAdminMixin, ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
        "position",
    )
    ordering = ("position",)
    list_editable = ("position",)
    search_fields = ("title", "description")
    list_filter = ("is_active",)
    autocomplete_fields = ("stations",)
    # fieldsets = (
    #     ("Basic Info", {"fields": ("video", "views", "position")}),
    #     ("Timestamps", {"fields": ("created_at", "updated_at")}),
    # )
    #
    # readonly_fields = ("created_at", "updated_at")
