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


def chart_list(req):
    return render(req, "chart_list.html")

def chart_bar(req):
    """构造柱状图数据"""
    #这里我们用一个列表来模拟从数据库里面获取数据
    legend=["Jack","Mary"]
    series_list = [
          {
            "name": 'Jack',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
          },
          {
            "name": 'Mary',
            "type": 'bar',
            "data": [3, 8, 26, 15, 7, 30]
          }
        ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        "status":True,
        "data":{
            "legend":legend,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }

    return JsonResponse(result)