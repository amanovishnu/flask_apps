from django.http import HttpResponse
from datetime import datetime


def server_time(request):
    response = datetime.now()
    return HttpResponse(response)
