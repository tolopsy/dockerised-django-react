from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def test_view(request):
    return HttpResponse("working")

def json_test_view(request):
    return JsonResponse({"active": True})