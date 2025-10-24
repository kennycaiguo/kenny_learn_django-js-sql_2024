"""
把所有表单相关的类都放在这里,方便views.py的函数调用,而且不会使得views.py过于臃肿
"""
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from day16app.utils.basemodelform import BootstrapModelForm
from django import forms
from day16app import models
from day16app.models import UserInfo, Department


# 使用django ModelForm组件的写法
# 1.定义一个表单类继承自forms.ModelForm
class UserInfoForm(BootstrapModelForm):
    """添加用户和编辑用户信息需要使用的类"""
    name = forms.CharField(min_length=2, label="姓名")  # 设置姓名的最小长度
    create_time = forms.CharField(
        min_length=10, label="入职时间",
        widget=forms.TextInput(attrs={"autocomplete": "off"})
    )

    class Meta:
        model = UserInfo
        fields = ['name', "password", "age", "account", "create_time", "gender", "dep"]


# 操作PrettyNumber添加数据的ModelForm类
class PrettyNumberAddForm(BootstrapModelForm):
    # 添加验证器方式1. 正则表达式 ,验证手机号格式
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        model = models.PrettyNumber
        # fields = ['mobile', "price", "level", "status"]
        fields = "__all__"  # 也可以这么写,表示模型中所有的字段都需要

    # # 添加验证方式2,钩子函数,验证手机号码是否已经存在,(当然也可以验证手机号格式,这里不是验证手机号格式)
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exist = models.PrettyNumber.objects.filter(mobile=txt_mobile).exists()
        if exist:
            raise ValidationError("手机号已经存在,不能重复")  # 验证失败就抛异常
        return txt_mobile  # 验证通过就把他返回


# 编辑靓号功能需要用到的类
class PrettyNumberEditForm(BootstrapModelForm):
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


class AdminAddForm(BootstrapModelForm):
    # 核对2次输入密码是否一致
    confirm_pwd = forms.CharField(
        label="确认密码",
        # widget=forms.PasswordInput(render_value=True)  #密码验证不通过后不让他清空,其实清空更好
        widget=forms.PasswordInput  # 不显示密码
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_pwd"]
        widgets = {
            # "password": forms.PasswordInput(render_value=True)  #密码验证不通过后不让他清空,其实清空更好
            "password": forms.PasswordInput  # 把密码字段也隐藏
        }

    # 管理员账户不能重复,钩子函数来的
    def clean_username(self):
        txt_username = self.cleaned_data["username"]
        exist = models.Admin.objects.filter(username=txt_username).exists()
        if exist:
            raise ValidationError("用户名不能重复")  # 验证失败就抛异常
        return txt_username  # 验证通过就把他返回

    # 确认密码的钩子
    def clean_confirm_pwd(self):
        password = self.cleaned_data["password"]
        confirm_pwd = self.cleaned_data["confirm_pwd"]
        if confirm_pwd != password:
            raise ValidationError("确认密码和原来的密码不一样")  # 验证失败就抛异常
        return confirm_pwd


class AdminEditForm(BootstrapModelForm):
    class Meta:
        model = models.Admin
        fields = "__all__"

    # 管理员账户不能重复
    def clean_username(self):
        txt_username = self.cleaned_data["username"]
        exist = models.Admin.objects.exclude(id=self.instance.pk).filter(username=txt_username).exists()
        if exist:
            raise ValidationError("用户名不能重复")  # 验证失败就抛异常
        return txt_username  # 验证通过就把他返回
