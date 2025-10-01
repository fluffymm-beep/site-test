from django.db import models


class Category(models.Model):
    """Grouping of prompts displayed in the gallery."""

    name = models.CharField("نام دسته", max_length=100)
    description = models.TextField("توضیحات", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "دسته"
        verbose_name_plural = "دسته‌ها"

    def __str__(self) -> str:
        return self.name


class Prompt(models.Model):
    """Reusable ChatGPT prompt curated for the gallery."""

    category = models.ForeignKey(
        Category,
        related_name="prompts",
        on_delete=models.CASCADE,
        verbose_name="دسته",
    )
    title = models.CharField("عنوان", max_length=150)
    content = models.TextField("متن پرامپت")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "پرامپت"
        verbose_name_plural = "پرامپت‌ها"

    def __str__(self) -> str:
        return self.title
