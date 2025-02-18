from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from unfold.admin import ModelAdmin

admin.site.unregister(Group)
admin.site.unregister(Site)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_vertical = ("permissions",)


@admin.register(Site)
class SiteAdmin(ModelAdmin):
    list_display = ("id", "domain", "name")
    search_fields = ("domain", "name")
    list_filter = ("domain", "name")
