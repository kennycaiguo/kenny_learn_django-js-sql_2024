import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.encrypt import md5
from day16app.utils.pagination import Pagination
from day16app.utils.day16forms import OrderModelForm
from day16app.utils.code import check_code
from io import BytesIO
from django import forms
from day16app.utils.basemform import BootstrapForm


def order_list(req):
    form = OrderModelForm()
    return render(req, "order_list.html", {"form": form})

@csrf_exempt
def order_add(req):
    """新增订单的后台处理函数Ajax提交方式"""
    print(req.POST)
    form = OrderModelForm(data=req.POST)
    if form.is_valid():
        form.save()  # 表单验证(主要是不让数据为空)通过,就保存数据
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status":False,"errors":form.errors}
    return HttpResponse(json.dumps(data_dict)) # 验证失败就返回错误信息