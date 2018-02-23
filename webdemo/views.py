from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("Hello, world. This is Demo Application.")


def index(request):
    return HttpResponse(datetime.datetime.now().strftime("%H:%M:%S"))
