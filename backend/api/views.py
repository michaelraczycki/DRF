import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    data ={}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    return JsonResponse(data)

