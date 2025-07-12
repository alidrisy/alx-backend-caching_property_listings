from django.core.cache import cache
from properties.models import Property


def get_all_properties():
    all_properties = cache.get("all_properties")
    if all_properties:
        return all_properties
    queryset = Property.objects.all()
    cache.set("all_properties", queryset, 3600)
    return queryset
