from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.http import JsonResponse
from products.models import Product
# Create your views here.
@csrf_exempt
def api_view(request, *args, **kwargs):
    from_basic=request.body
    data = {}
    try:
        data = json.loads(from_basic) #converting JSON data to python dictionary
    except:
        pass
    print(data.keys())
    print(request.headers)
    print(request.content_type)
    data["content_type"] = request.content_type
    data["headers"] = dict(request.headers)
    data["params"] = request.GET
    print(request.GET)
    return JsonResponse(data)

@csrf_exempt
def model_api(request, *args, **kwargs):
    random_model_instance = Product.objects.all().order_by("?").first()#randomly select a model instance(ORM)
    data = {}
    if random_model_instance:
        data["title"] = random_model_instance.title
        data["description"] = random_model_instance.content
        data["price"] = random_model_instance.price
        return JsonResponse(data)
