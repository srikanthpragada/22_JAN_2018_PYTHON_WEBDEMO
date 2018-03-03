from .dbmodel import DbCourse
from django.shortcuts import render
from .forms import AddCourseForm, AddAccountForm
from demo.models import Account
from django.db.models import Sum, Count

import sqlite3


def home(request):
    context = Account.objects.all().aggregate(total=Sum('balance'),
                                              count=Count('customer'))
    return render(request, 'demo/home.html', context)


def list_accounts(request):
    return render(request, 'demo/list_accounts.html',
                  {'accounts' : Account.objects.all()})


def add_account(request):
    message = ""
    if request.method == "POST":
        f = AddAccountForm(request.POST)
        if f.is_valid():
            f.save()  # Save to table and commit
            message = "Added Account Successfully!"

    else:
        f = AddAccountForm()
    return render(request, 'demo/add_account.html', {'form': f, 'message': message})
