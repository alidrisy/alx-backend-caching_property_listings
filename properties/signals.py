from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from properties.models import Property


@receiver(post_save, sender=Property)
def clear_cache_on_save(sender, instance):
    cache.delete("all_properties")


@receiver(post_delete, sender=Property)
def clear_cache_on_delete(sender, instance):
    cache.delete("all_properties")
