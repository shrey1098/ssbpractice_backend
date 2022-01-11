from django.http import JsonResponse
from backend.services import getWat, getSrt


# Create your views here.


def get_wat(request):
    words = getWat()
    return JsonResponse(words)

def get_srt(request):
    situations = getSrt()
    return JsonResponse(situations)