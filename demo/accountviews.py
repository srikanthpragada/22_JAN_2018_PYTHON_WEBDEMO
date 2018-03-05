from .dbmodel import DbCourse
from django.shortcuts import render
from .forms import AddCourseForm, AddAccountForm, AddTransactionForm
from demo.models import Account, Transaction
from django.db.models import Sum, Count

import sqlite3


def home(request):
    context = Account.objects.all().aggregate(total=Sum('balance'),
                                              count=Count('customer'))
    return render(request, 'demo/home.html', context)


def list_accounts(request):
    return render(request, 'demo/list_accounts.html',
                  {'accounts' : Account.objects.all()})

def transactions_by_account(request,id):
    return render(request, 'demo/transactions_by_account.html',
                  {'id' : id,
                   'transactions' : Transaction.objects.filter(account__id = id)})

def edit_trans(request,id):
    message = ""
    if request.method == "POST":
        f = AddTransactionForm(request.POST)
        if f.is_valid():
            f.save()  # Save to table and commit
            message = "Update Transactions Successfully!"

    else:
        trans = Transaction.objects.get(pk = id)
        f = AddTransactionForm(trans)
    return render(request, 'demo/edit_trans.html', {'form': f, 'message': message})



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


def add_transaction(request):
    message = ""
    if request.method == "POST":
        f = AddTransactionForm(request.POST)
        if f.is_valid():
            f.save()  # Save to table and commit
            message = "Added Transactions Successfully!"

    else:
        f = AddTransactionForm()
    return render(request, 'demo/add_transaction.html', {'form': f, 'message': message})
