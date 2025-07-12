from django.shortcuts import render

from properties.utils import get_all_properties
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)
def property_list(request):
    all_property = get_all_properties()
    return render(request, "products.html", {"products": all_property})
