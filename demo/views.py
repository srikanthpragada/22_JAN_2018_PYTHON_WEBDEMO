from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Demo Application!")


def course(request):
    return render(request,"demo/course.html")
