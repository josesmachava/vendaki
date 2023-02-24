from typing import List

from ninja import NinjaAPI
from ninja.orm import create_schema

from dashboard.models import Product

api = NinjaAPI()

ProductSchema = create_schema(Product)


@api.get("/products", response=List[ProductSchema])
def list_products(request):
    product = Product.objects.all()
    return product
