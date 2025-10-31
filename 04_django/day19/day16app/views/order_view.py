import json
import random
from datetime import datetime
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
    #获取所有数据
    orders = models.Order.objects.all().order_by("-id") # 倒序排列
    #分页
    page_obj = Pagination(req, orders,page_size=5)
    page_query_set = page_obj.page_queryset
    # 分页功能
    page_str = page_obj.gen_html()
    form = OrderModelForm()
    context = {
        "form":form,
        "orders":page_query_set,
        "page_str":page_str
    }
    #渲染数据
    return render(req, "order_list.html", context)

@csrf_exempt
def order_add(req):
    """新增订单的后台处理函数Ajax提交方式"""
    print(req.POST)
    form = OrderModelForm(data=req.POST)
    if form.is_valid():
        # 生成oid并且添加到form的数据中
        oid = datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randint(1000,9999))
        form.instance.oid = oid
        # 从session在获取当前登录的管理员的id
        # admin =req.session.get("info")
        # # print(req.session.get("info"))
        # form.instance.admin_id = admin.get("id")
        form.instance.admin_id = req.session["info"]["id"] # 也可以这么写
        form.save()  # 表单验证(主要是不让数据为空)通过,就保存数据

        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status":False,"errors":form.errors}
    return HttpResponse(json.dumps(data_dict)) # 验证失败就返回错误信息