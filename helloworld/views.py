from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    data = { 'Message': 'Hello World!' }
    return JsonResponse(data)