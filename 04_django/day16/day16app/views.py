from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from day16app.models import Department, UserInfo  # 这两个是上一次导入的,不改了
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from django import forms


# Create your views here.

def home(req):
    return render(req, "home.html")


def index(req):
    return render(req, "home.html")


def dep_list(req):
    """显示部门列表"""
    dep_list = Department.objects.all()
    return render(req, "dep_list.html", {"deps": dep_list})


def dep_add(req):
    """新增部门"""
    # get
    if req.method == "GET":
        return render(req, "dep_add.html")
    # post
    title = req.POST.get("title")
    Department.objects.create(title=title)
    return redirect("/dep/list")


def dep_del(req):
    """删除部门"""
    nid = req.GET.get("nid")
    Department.objects.filter(id=nid).delete()
    return redirect("/dep/list")


# 写法1.
# def dep_edit(req):
#     # 处理get
#     if req.method == "GET":
#         nid = req.GET.get("nid")
#         dep = Department.objects.filter(id=nid).first()
#         return render(req, "dep_edit.html", {"dep": dep})
#     # 处理post
#     id = req.POST.get("id")
#     title = req.POST.get("title")
#     Department.objects.filter(id=id).update(title=title)
#     return redirect("/dep/list")

# 写法2
def dep_edit(req, nid):
    # 处理get
    if req.method == "GET":
        dep = Department.objects.filter(id=nid).first()
        return render(req, "dep_edit.html", {"dep": dep})
    # 处理post
    # id T= req.POS.get("id")  # 在模板里面没有使用hidden字段,这里就不需要这一句
    title = req.POST.get("title")
    Department.objects.filter(id=nid).update(title=title)
    return redirect("/dep/list")


def user_list(req):
    users = UserInfo.objects.all()
    # 数据库里面拿到的时间格式不太好,我们需要把它转化为字符串格式
    # for user in users:
    #     user.create_time = user.create_time.strftime("%Y-%m-%d %H:%M:%S")
    return render(req, "user_list.html", {'users': users})


# 这个是最原始的写法
# def user_add(req):
#     if req.method == "GET":
#         context = {
#             "g_choice":UserInfo.gender_choices,
#             "deps": Department.objects.all()
#         }
#         return render(req, "user_add.html",context)
#     # 获取post请求的数据并且保存
#     name = req.POST.get("name")
#     pwd = req.POST.get("pwd")
#     age = req.POST.get("age")
#     acc = req.POST.get("acc")
#     ctime = req.POST.get("ctime")
#     gender = req.POST.get("gender")
#     dep = req.POST.get("dep")
#     UserInfo.objects.create(name=name,password=pwd,age=age,account=acc,create_time=ctime,gender=gender,dep_id=dep)
#     return redirect("/user/list")

# 使用django ModelForm组件的写法
# 1.定义一个表单类继承自forms.ModelForm
class UserInfoForm(forms.ModelForm):
    name = forms.CharField(min_length=2, label="姓名")  # 设置姓名的最小长度

    class Meta:
        model = UserInfo
        fields = ['name', "password", "age", "account", "create_time", "gender", "dep"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_add(req):
    """新增用户"""
    if req.method == "GET":
        form = UserInfoForm()
        return render(req, "user_add.html", {"form": form})
    # 获取post请求的数据并且进行数据校验
    form = UserInfoForm(data=req.POST)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/user/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "user_add.html", {"form": form})


def user_edit(req, nid):
    """编辑用户信息"""
    # 查询数据
    user1 = UserInfo.objects.filter(id=nid).first()  # 放在这里是因为有2个地方需要用到这个user1
    if req.method == "GET":
        form = UserInfoForm(instance=user1)
        return render(req, "user_edit.html", {"form": form, "nid": nid})
    # 获取post请求的数据并且进行数据校验
    form = UserInfoForm(instance=user1, data=req.POST)  # 更新的时候需要两个参数来构造form对象:数据和需要更新的实例
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save()  # 新增和更新都是使用这个方法,只是form里面的数据不一样
        return redirect("/user/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "user_edit.html", {"form": form})


def user_del(req, nid):
    """删除用户信息"""
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


# 靓号管理函数
def pretty_list(req):
    """靓号列表"""
    pretty_data = models.PrettyNumber.objects.all().order_by("-id")
    return render(req, "pretty_list.html", {"pretties": pretty_data})


# 操作PrettyNumber数据的ModelForm类
class PrettyNumberForm(forms.ModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )
    class Meta:
        model = models.PrettyNumber
        # fields = ['mobile', "price", "level", "status"]
        fields = "__all__"  # 也可以这么写,表示模型中所有的字段都需要

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def pretty_add(req):
    """新增靓号"""
    if req.method == "GET":
        form = PrettyNumberForm()
        return render(req, "pretty_add.html", {"form": form})
    # 获取post请求的数据并且进行数据校验
    form = PrettyNumberForm(data=req.POST)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "pretty_add.html", {"form": form})


def pretty_edit(req, nid):
    """修改靓号"""
    pretty_num = models.PrettyNumber.objects.filter(id=nid).first()
    if req.method == "GET":
        form = PrettyNumberForm(instance=pretty_num)
        return render(req, "pretty_edit.html", {"form": form,"nid":nid})
    # 获取post请求的数据并且进行数据校验
    form = PrettyNumberForm(data=req.POST,instance=pretty_num)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "pretty_edit.html", {"form": form})
