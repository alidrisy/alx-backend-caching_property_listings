import logging
from django.core.cache import cache
from properties.models import Property
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)


def get_all_properties():
    all_properties = cache.get("all_properties")
    if all_properties:
        return all_properties
    queryset = Property.objects.all()
    cache.set("all_properties", queryset, 3600)
    return queryset


def get_redis_cache_metrics():
    try:
        redis_conn = get_redis_connection("default")

        info = redis_conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": hit_ratio,
        }

        logger.info(f"Redis Cache Metrics: {metrics}")

        return metrics

    except Exception as e:
        logger.error(f"Error fetching Redis cache metrics: {e}")
        return None
