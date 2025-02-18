from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Advertisement(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), db_index=True)
    video = models.FileField(
        upload_to="videos/",
        verbose_name=_("Video"),
        validators=[FileExtensionValidator(["mp4", "mkv", "mov"])],
    )
    duration = models.BigIntegerField(
        verbose_name=_("Duration"), db_index=True, null=True, blank=True
    )
    hls = models.FileField(
        upload_to="hls/", verbose_name=_("HLS"), null=True, blank=True
    )
    views = models.BigIntegerField(verbose_name=_("Views"), db_index=True, default=0)
    position = models.BigIntegerField(
        verbose_name=_("Position"), db_index=True, default=0
    )
    is_active = models.BooleanField(
        default=True, verbose_name=_("Is Active"), db_index=True
    )
    stations = models.ManyToManyField(
        "Station",
        related_name="advertisements",
        verbose_name=_("Stations"),
        blank=True,
        db_index=True,
    )

    class Meta:
        db_table = "advertisement"
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")
        ordering = ["position"]

    def __str__(self) -> str:
        return str(self.name)
