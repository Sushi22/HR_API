from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.renderers import JSONRenderer
from get_api.info import my_data
from django.http import JsonResponse
import json
# Create your views here.

def get_hr_data(request):
    # print("heloo")
    print(my_data)
    if request.method=="GET":
        return JsonResponse(my_data)



