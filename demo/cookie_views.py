from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect


def list_cookies(request):
    data = request.COOKIES
    return render(request, 'demo/list_cookies.html', {'cookies': data})


def add_cookie(request):
    if request.method == "GET":
        return render(request, 'demo/add_cookie.html')
    else:
        # process data
        name = request.POST["cookie_name"]
        value = request.POST["cookie_value"]

        response = HttpResponseRedirect("/demo/list_cookies/")
        if 'durable' in request.POST:  # Checkbox is selected?
            # Create durable cookie
            response.set_cookie(name, value, expires=datetime.datetime.now() + datetime.timedelta(days=10))
        else:
            # Create browser-based cookie
            response.set_cookie(name, value)
        return response
