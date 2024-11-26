from django.core.cache import cache

from catalog.models import Categories
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    if not CACHE_ENABLED:
        return Categories.objects.all()
    categories = Categories.objects.all()
    for category in categories:
        key = f'context_data_{Categories.objects.get(pk=category.pk)}'
        categories = cache.get(key)
        if categories is not None:
            return categories
        categories = Categories.objects.all()
        cache.set(key, categories)
    return categories


