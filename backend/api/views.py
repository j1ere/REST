from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.http import JsonResponse

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
    return JsonResponse(data)
