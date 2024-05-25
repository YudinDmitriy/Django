from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    product_image = models.ImageField(
        upload_to="products/", verbose_name="Изображение", **NULLABLE
    )
    category = models.ForeignKey(
        'Categories',
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="products",
    )
    unit_price = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(verbose_name="Дата создания записи")
    updated_at = models.DateTimeField(verbose_name="Дата изменений записи")


    def __str__(self):
        return f"{self.product_name}({self.description})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "product_name", "unit_price"]


class Categories(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category_name"]
