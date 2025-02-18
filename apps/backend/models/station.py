from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Station(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), db_index=True)
    longitude = models.FloatField(verbose_name=_("Longitude"), db_index=True)
    latitude = models.FloatField(verbose_name=_("Latitude"), db_index=True)
    address = models.CharField(max_length=255, verbose_name=_("Address"), db_index=True)
    paper_count = models.BigIntegerField(verbose_name=_("Paper Count"), db_index=True)
    is_active = models.BooleanField(
        default=True, verbose_name=_("Is Active"), db_index=True
    )

    class Meta:
        db_table = "station"
        verbose_name = _("Station")
        verbose_name_plural = _("Stations")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.id} - {self.name} - {self.address}"


class StationCredential(AbstractBaseModel):
    station = models.OneToOneField(
        Station,
        on_delete=models.CASCADE,
        related_name="station_credentials",
        verbose_name=_("Station"),
    )
    auth_uri = models.CharField(max_length=255, verbose_name=_("Auth URI"))
    client_id = models.CharField(max_length=255, verbose_name=_("Client ID"))
    secret = models.CharField(max_length=255, verbose_name=_("Secret"))
    device = models.CharField(max_length=255, verbose_name=_("Device"))
    host = models.CharField(max_length=255, verbose_name=_("Host"))
    password = models.CharField(max_length=255, verbose_name=_("Password"))

    class Meta:
        db_table = "station_credential"
        verbose_name = _("Station Credential")
        verbose_name_plural = _("Station Credentials")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(self.station)
