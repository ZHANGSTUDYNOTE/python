import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import userInfo


# Create your views here.

def register(request):
    return render(request, 'userInfo/register.html')


def registerData(request):
    # for i in range(0, 10):
    #     user = userInfo()
    #     user.email = '123@qq.com'
    #     user.mobile = '13119076476'
    #     user.name = 'zpc'
    #     user.password = '123456a'
    #     user.save()
    resp = {'code': 200, 'message': 'ok', 'data': {'list': list(userInfo.objects.values().values())}}
    return JsonResponse(resp, safe=False)
