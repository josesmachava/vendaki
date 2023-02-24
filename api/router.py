from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/products")
def get_products(request):
    return "Hello world"
