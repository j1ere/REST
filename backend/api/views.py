from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse, HttpResponse
from products.models import Product
# Create your views here.
@csrf_exempt
def custom_api_view(request, *args, **kwargs):
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

@csrf_exempt
def model_api_serialized(request, *args, **kwargs):
    client = request.body
    print(json.loads(client))

    random_model_instance = Product.objects.all().order_by("?").first()
    data = {}
    if random_model_instance:
        data = model_to_dict(random_model_instance, fields=['title', 'price'])#specify fields to send
    return JsonResponse(data)

@api_view(["POST"])
@csrf_exempt
def model_api_drf(request, *args, **kwargs):
    client = request.body
    print(f"{json.loads(client)}")
    random_model_instance = Product.objects.all().order_by("?").first()
    data = {}
    if random_model_instance:
        data = model_to_dict(random_model_instance)
    return Response(data)


"""
django rest framework serializers(modelserializers)
"""
from rest_framework import generics
from products.models import Book
from products.serializers import BookSerializer, MyBookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MyBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(publish_date__isnull=True)
    serializer_class = MyBookSerializer