from django.contrib import admin
from django.db.models import Count

from .models import Category, Prompt


class PromptInline(admin.TabularInline):
    model = Prompt
    extra = 1
    fields = ("title", "content")
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "prompt_count", "updated_at")
    search_fields = ("name", "description")
    inlines = (PromptInline,)
    readonly_fields = ("created_at", "updated_at")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(prompt_total=Count("prompts"))

    @admin.display(description="تعداد پرامپت‌ها", ordering="prompt_total")
    def prompt_count(self, obj):
        return getattr(obj, "prompt_total", obj.prompts.count())


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "updated_at")
    list_filter = ("category",)
    search_fields = ("title", "content")
    raw_id_fields = ("category",)
    readonly_fields = ("created_at", "updated_at")
