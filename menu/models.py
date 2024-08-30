from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    title = models.CharField("Название", max_length=25)
    url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Прямой URL",
    )
    named_url = models.CharField(
        "Именованный URL",
        max_length=100,
        blank=True,
        null=True,
        help_text="URL через reverse",
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name="Родитель",
    )
    menu_name = models.CharField("Название меню", max_length=25)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url
