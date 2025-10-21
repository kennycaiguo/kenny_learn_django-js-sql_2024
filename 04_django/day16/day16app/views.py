from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
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


from day16app.addnum import addData


# 靓号管理函数,写法1.
# def pretty_list(req):
#     """靓号列表"""
#     # addData()
#     term = {}
#     kw = req.GET.get("kw", "")
#     if kw:
#         term["mobile__contains"] = kw
#     # res = models.PrettyNumber.objects.filter(**term)
#     # print(res)
#     # pretty_data = models.PrettyNumber.objects.filter(**term).order_by("-level") #filter方法当里面的条件为空就相当于all()方法
#     # 分页功能
#     page = int(req.GET.get("page", 1))  # 默认是第一页
#     page_size = 10  # 每一页需要显示的数量
#     start = (page - 1) * page_size  # 计算开位置
#     end = page * page_size  # 计算结束位置
#
#     pretty_data = models.PrettyNumber.objects.filter(**term).order_by("-level")[start:end]  # 只显示前页面从开始到结束之间的数据
#
#     # 获取总共有多少条数据
#     count = models.PrettyNumber.objects.filter(**term).order_by("-level").count()
#     # 计算总页数
#     page_count, remain = divmod(count, page_size)  # divmod(a,b)函数会计算 a/b然后返回一个元组(商,余数),我们可以用2个变量来接受,一个是商,另外一个是余数
#     if remain:
#         page_count += 1  # 如果余数不为0,总页数需要+1,即使余数是1也需要+1
#     # 计算出当前的显示范围
#     increment = 5
#     page_start = page - increment
#     if page_start < 1:
#         page_start = 1
#     page_end = page + increment
#     if page_end > page_count:
#         page_end = page_count
#     page_str_list = []
#     for i in range(page_start, page_end + 1):  # 这里page_count需要加1因为for...range不包括后面的值
#         if i == page:
#             el = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)  #如果是当前页面,我们给他添加一个样式
#         else:
#             el = '<li><a href="?page={}">{}</a></li>'.format(i, i)
#         page_str_list.append(el)
#         page_str = mark_safe("".join(page_str_list))
#
#     return render(req, "pretty_list.html", {"pretties": pretty_data, "kw": kw, "page_str": page_str})

# 靓号管理函数,写法2.
def pretty_list(req):
    """靓号列表"""
    # addData()
    term = {}
    kw = req.GET.get("kw", "")
    if kw:
        term["mobile__contains"] = kw
    # res = models.PrettyNumber.objects.filter(**term)
    # print(res)
    # pretty_data = models.PrettyNumber.objects.filter(**term).order_by("-level") #filter方法当里面的条件为空就相当于all()方法
    # 分页功能
    page = int(req.GET.get("page", 1))  # 默认是第一页
    page_size = 10  # 每一页需要显示的数量
    start = (page - 1) * page_size  # 计算开位置
    end = page * page_size  # 计算结束位置

    pretty_data = models.PrettyNumber.objects.filter(**term).order_by("-level")[start:end]  # 只显示前页面从开始到结束之间的数据

    # 获取总共有多少条数据
    count = models.PrettyNumber.objects.filter(**term).order_by("-level").count()
    # 计算总页数
    page_count, remain = divmod(count, page_size)  # divmod(a,b)函数会计算 a/b然后返回一个元组(商,余数),我们可以用2个变量来接受,一个是商,另外一个是余数
    if remain:
        page_count += 1  # 如果余数不为0,总页数需要+1,即使余数是1也需要+1
    # 计算出当前的显示范围
    incr = 5
    if page_count <= 2 * incr + 1:  # 数据库的数据比较少的时候
        page_start = 1
        page_end = page_count
    else:
        # 数据库的数据比较多
        if page <= incr: #当前页码比增量还小或者等于增量,就把起始页码固定为1
            page_start = 1
            page_end = 2 * incr +1
        else:
            if (page+5) > page_count:
                page_start = page_count - 2 * incr
                page_end = page_count
            else:
                page_start = page - incr
                page_end = page + incr

    page_str_list = []
    # 首页
    first = '<li><a href="?page={}">首页</a></li>'.format(1)
    page_str_list.append(first)
    # 上一页
    if page > 1:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(page-1)
    else:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)

    for i in range(page_start, page_end + 1):  # 这里page_count需要加1因为for...range不包括后面的值
        if i == page:
            el = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)  # 如果是当前页面,我们给他添加一个样式
        else:
            el = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(el)
        # page_str = mark_safe("".join(page_str_list))

    # 下一页
    if page >= page_count:
        next = '<li><a href="?page={}">下一页</a></li>'.format(page_count)
    else:
        next = '<li><a href="?page={}">下一页</a></li>'.format(page+1)
    page_str_list.append(next)

    # 尾页
    last = '<li><a href="?page={}">尾页</a></li>'.format(page_count)
    page_str_list.append(last)
    page_str = mark_safe("".join(page_str_list))
    return render(req, "pretty_list.html", {"pretties": pretty_data, "kw": kw, "page_str": page_str})


# 操作PrettyNumber数据的ModelForm类
class PrettyNumberAddForm(forms.ModelForm):
    # 添加验证器方式1. 正则表达式 ,验证手机号格式
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

    # # 添加验证方式2,钩子函数,验证手机号码是否已经存在,(当然也可以验证手机号格式,这里不是验证手机号格式)
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exist = models.PrettyNumber.objects.filter(mobile=txt_mobile).exists()
        if exist:
            raise ValidationError("手机号已经存在,不能重复")  # 验证失败就抛异常
        return txt_mobile  # 验证通过就把他返回


def pretty_add(req):
    """新增靓号"""
    if req.method == "GET":
        form = PrettyNumberAddForm()
        return render(req, "pretty_add.html", {"form": form})
    # 获取post请求的数据并且进行数据校验
    form = PrettyNumberAddForm(data=req.POST)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "pretty_add.html", {"form": form})


class PrettyNumberEditForm(forms.ModelForm):
    # 添加验证器方式1. 正则表达式 ,验证手机号格式
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    #     disabled=True  # 不允许编辑手机号
    # )
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
        disabled=False  # 允许编辑手机号
    )

    class Meta:
        model = models.PrettyNumber
        # fields = ['mobile', "price", "level", "status"]
        fields = "__all__"  # 也可以这么写,表示模型中所有的字段都需要

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # # 添加验证方式2,钩子函数,验证手机号格式的另外一种方式
    # def clean_mobile(self):
    #     txt_mobile = self.cleaned_data["mobile"]
    #     if len(txt_mobile) !=11:
    #         raise ValidationError("手机号格式错误")  # 验证失败就抛异常
    #     return txt_mobile  # 验证通过就把他返回

    # 排除自己以外,手机号不能重复(有点绕,慢慢体会)
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exist = models.PrettyNumber.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exist:
            raise ValidationError("手机号已经存在,不能重复")  # 验证失败就抛异常
        return txt_mobile  # 验证通过就把他返回


def pretty_edit(req, nid):
    """修改靓号"""
    pretty_num = models.PrettyNumber.objects.filter(id=nid).first()
    if req.method == "GET":
        form = PrettyNumberEditForm(instance=pretty_num)
        return render(req, "pretty_edit.html", {"form": form})  # 使用了验证器,这里就不要传递nid,获取不到的.
    # 获取post请求的数据并且进行数据校验
    form = PrettyNumberEditForm(data=req.POST, instance=pretty_num)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "pretty_edit.html", {"form": form})


def pretty_del(req, nid):
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")
