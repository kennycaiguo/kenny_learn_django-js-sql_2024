from django.db import models


class Admin(models.Model):
    """管理员表"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密  码", max_length=64)


# Create your models here.
class Department(models.Model):
    """部门表"""
    # id = models.BigAutoField(verbose_name="ID",primary_key=True)  #不需要写django会自动处理这个表字段
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")  # 需要添加默
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2)
    create_time = models.DateField(verbose_name="入职时间")  # 把原来的DateTimeField改为DateField
    # 这个类型不对,它是没有约束的
    # dep_id=models.BigIntegerField(verbose_name="部门ID")
    # 这个类型有约束的,也就是外键
    # 只需要写dep,然后django会把它变为dep_id
    # 方式1,需要设置关联的表(类),还要设置表的关联的列,还需要设置部门被删除了,对应的员工数据会级联删除.
    dep = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE, default="选择部门")
    # 方式2.需要设置关联的表(类),还要设置表的关联的列,还需要设置可以置空,也就是部门被删除了,对应员工的部门变为空
    # dep = models.ForeignKey(to="Department", to_field="id",null=True,blank=True, on_delete=models.SET_NULL)
    gender_choices = (
        (0, "女"),
        (1, "男")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, default="选择性别")  # 注意django中性别的处理方式


# 靓号类
class PrettyNumber(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name="手机号码", max_length=11)
    price = models.IntegerField(verbose_name="价钱",default=2000)
    level_choice = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
        (4, "四级"),
    )
    level = models.SmallIntegerField(verbose_name="靓号等级", choices=level_choice, default=1)
    status_choice = (
        (0, "未占用"),
        (1, "已使用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choice, default=0)

