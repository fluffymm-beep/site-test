from django.db.models import Prefetch, Q
from django.shortcuts import render

from .models import Category, Prompt


def prompt_list(request):
    """Render a gallery of curated ChatGPT prompt ideas."""

    quick_tips = [
        "در هر پرامپت نقش و مخاطب را مشخص کنید.",
        "درخواست خود را با مثال یا قالب خروجی روشن همراه کنید.",
        "با افزودن محدودیت زمانی یا تعداد خروجی، پاسخ دقیق‌تر می‌شود.",
    ]

    search_query = request.GET.get("q", "").strip()

    prompt_queryset = Prompt.objects.select_related("category").order_by("title")
    if search_query:
        prompt_queryset = prompt_queryset.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )

    prefetch = Prefetch("prompts", queryset=prompt_queryset, to_attr="display_prompts")
    categories_queryset = Category.objects.order_by("name").prefetch_related(prefetch)

    categories = []
    total_prompts = 0
    for category in categories_queryset:
        prompts = list(getattr(category, "display_prompts", []))
        if search_query and not prompts:
            continue
        total_prompts += len(prompts)
        category.prompts_for_display = prompts
        categories.append(category)

    context = {
        "page_title": "گالری پرامپت‌های ChatGPT",
        "categories": categories,
        "quick_tips": quick_tips,
        "search_query": search_query,
        "total_prompts": total_prompts,
        "is_search": bool(search_query),
    }

    return render(request, "prompts/prompt_list.html", context)
