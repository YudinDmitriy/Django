from django.db import models

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to="preview/", verbose_name="Превью", **NULLABLE)
    created_at = models.DateTimeField(verbose_name="Дата создания записи", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
