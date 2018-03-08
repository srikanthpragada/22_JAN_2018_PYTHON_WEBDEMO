from django.http import JsonResponse, HttpResponse
from demo.models import Account
from demo.serializers import AccountSerializer


def list_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_account(request, pk):
    try:
        account = Account.objects.get(pk=pk)
        if request.method == 'DELETE':
             print("Deleting ", pk)
             return HttpResponse(status=200)
        else:
             serializer = AccountSerializer(account)
             return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)
