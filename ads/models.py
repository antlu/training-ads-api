from django.db import models
from django.utils import timezone


class Advertisement(models.Model):
    """An ad model."""

    title = models.CharField("Название", max_length=200)  # noqa: WPS432
    description = models.CharField("Описание", max_length=1000, blank=True)
    price = models.PositiveIntegerField("Цена")
    photo_link1 = models.URLField("Ссылка на фото 1")
    photo_link2 = models.URLField("Ссылка на фото 2", blank=True)
    photo_link3 = models.URLField("Ссылка на фото 3", blank=True)
    created_at = models.DateTimeField("Создано", default=timezone.now)

    def __str__(self):
        """Return string representation."""
        return self.title
