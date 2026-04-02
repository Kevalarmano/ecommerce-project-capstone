from django.http import JsonResponse
from .models import Product

def get_products(request):
    """
    Retrieve all products from the database.

    Returns:
        JSON response containing all products.
    """
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)