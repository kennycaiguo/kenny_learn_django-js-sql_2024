import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.encrypt import md5
from day16app.utils.pagination import Pagination
from day16app.utils import day16forms
from day16app.utils.code import check_code
from io import BytesIO
from django import forms
from day16app.utils.basemform import BootstrapForm


def task_list(req):
    return render(req, "task_list.html")


def task_test_list(req):
    return render(req, "task_test_list.html")


@csrf_exempt
def task_test_ajax(req):
    # 这里获取get请求的参数然后返回给用户
    # n1 = req.GET.get("n1")
    # n2 = req.GET.get("n2")
    # 获取post请求参数
    n1 = req.POST.get("n1")
    n2 = req.POST.get("n2")
    data_dict = {"status": "ok", "data": {"n1": n1, "n2": n2}}

    # return HttpResponse(json.dumps(data_dict))
    return JsonResponse(data_dict)


# 响应ajax带表单的请求
@csrf_exempt
def task_test_ajax2(req):
    print(req.POST)
    data_dict = {"status": "ok", "data": req.POST}
    return HttpResponse(json.dumps(data_dict))
    # return JsonResponse(req.POST) #这个有时候比如这里是不好用的.还是上面的好用


@csrf_exempt
def task_ajax(req):

    # return HttpResponse(json.dumps(data_dict))
    return JsonResponse()
