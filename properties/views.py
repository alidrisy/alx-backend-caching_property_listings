from django.shortcuts import render
from .models import Property
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)
def property_list(request):
    all_property = Property.objects.all()
    return render(request, "products.html", {"products": all_property})
