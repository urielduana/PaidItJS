from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from logica import test
# Create your views here.
def index(request):
    response ={
        "status": "success",
        "code": 200,
        "data": test.f()
    }

    return JsonResponse(response)