from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator

import datetime


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello! This is class view!')


class GreetView(View):
    greeting = 'Good Morning'
    template_name = "demoapp/greet.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name);

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        uname = request.POST["uname"]
        hour = datetime.time().hour
        if hour > 12 and hour < 17:
            self.greeting = "Good Afternoon"
        elif hour >= 17:
            self.greeting = "Good Evening"

        return render(request, self.template_name, {"greeting": self.greeting, "uname": uname});
