from django.shortcuts import render
from .forms import AddBookForm
# Create your views here.
from django.http import HttpResponse
from .models import Course


def index(request):
    return HttpResponse("Demo Application!")


def course(request):
    return render(request, "demo/course.html")


def course_list(request):
    courses = [Course("Python", 40, 5000), Course("Angular", 12, 3000)]
    return render(request, "demo/course_list.html", {"courses": courses})


def course_info(request):
    course = Course("Python Programming", 40, 5000,
                    ["OOP", "Data Structures", "Web Programming"])
    discount = course.price * 0.10
    netprice = course.price - discount
    context = {"course": course,
               "discount": discount,
               "netprice": netprice}
    return render(request, "demo/course_info.html", context)


def add_book(request):
    if request.method == "POST":
        f = AddBookForm(request.POST)    # bound form
        if f.is_valid():
            print("Valid")
        else:
            print("Invalid form")
            print(f.errors)
    else:
        f = AddBookForm()

    return render(request, 'demo/add_book.html', {'form': f})
