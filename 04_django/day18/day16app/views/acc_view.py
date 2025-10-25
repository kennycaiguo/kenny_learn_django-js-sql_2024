from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.encrypt import md5
from day16app.utils.pagination import Pagination
from day16app.utils import day16forms
from django import forms
from day16app.utils.basemform import BootstrapForm


class LoginForm(BootstrapForm):
    # 这里的字段名一定要和表单里面的name一样,并且要和Admin类里面的字段名一样,否则后面很难操作
    username = forms.CharField(label="用户名", widget=forms.TextInput)
    password = forms.CharField(label="密 码", widget=forms.PasswordInput)

    def clean_password(self):
        txt_pwd = self.cleaned_data.get("password")
        return md5(txt_pwd)  # 把获取到的密码进行md5加密


def login(req):
    if req.method == "GET":
        form = LoginForm()
        return render(req, "login.html", {"form": form})
    form = LoginForm(data=req.POST)
    if form.is_valid():
        # 普通form是没有save方法的,注意modelform才有
        # 写法1,
        # user = form.cleaned_data.get("username")
        # pwd = form.cleaned_data.get("password")
        # admin = models.Admin.objects.filter(username=user,password=pwd).first()

        # 写法2
        admin = models.Admin.objects.filter(**form.cleaned_data).first()
        # 如果用户名或者密码错误,就找不到数据.在渲染登录页面,也就是不让他跳转
        if not admin:
            form.add_error("password", "用户名或者密码错误!!!")  # 这个方法不需要修改模板的内容
            return render(req, "login.html", {"form": form})  # 用户信息验证失败,也就是登录失败
            # return render(req, "login.html", {"form": form,"error_msg":"用户名或者密码错误"})
        # 登录成功,生成随机字符串写到用户浏览器的cookie中,在django中这个操作比较简单.
        req.session["into"] = {"id": admin.id, "name": admin.username}
        return redirect("/admin/list/")  # 登录成功,跳转到管理员账户页面
    return render(req, "login.html", {"form": form})  # form表单校验失败
