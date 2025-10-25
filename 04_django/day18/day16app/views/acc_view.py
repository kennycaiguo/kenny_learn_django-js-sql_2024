from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.pagination import Pagination
from day16app.utils import day16forms
from django import forms
from day16app.utils.basemform import BootstrapForm


class LoginForm(BootstrapForm):
    username = forms.CharField(label="用户名", widget=forms.TextInput)
    password = forms.CharField(label="密 码", widget=forms.PasswordInput)


def login(req):
    if req.method == "GET":
        form = LoginForm()
        return render(req, "login.html", {"form": form})
    form = LoginForm(data=req.POST)
    if form.is_valid():
        #普通form是没有save方法的,注意modelform才有
        user = form.cleaned_data.get("username")
        pwd = form.cleaned_data.get("password")
        print(user,pwd)
        # models.Admin.objects.filter(username=user,password=pwd)
        return redirect("/admin/list/")
    return render(req, "login.html", {"form": form})
