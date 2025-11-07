import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from django import forms
from day16app.utils.basemform import BootstrapForm
import os



def upload_list(req):
    if req.method == "GET":
        return render(req, "upload_list.html")
    print(req.POST)
    print(req.FILES)
    file_obj = req.FILES.get("avatar")
    print(file_obj.name)  # 用name属性来获取文件名
    # 保存文件内容
    f = open("media\\" + file_obj.name, mode='wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse("上传成功")


class UploadForm(BootstrapForm):
    bootstrap_exclude_fields = ['img']  # 添加需要排除样式的字段
    name = forms.CharField(label="姓名", max_length=32)
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


def upload_form(req):
    form = UploadForm()
    if req.method == "GET":
        return render(req, "upload_form.html", {"form": form, "title": "利用django的Form组件实现文件上传"})
    form = UploadForm(data=req.POST, files=req.FILES)  # 文件上传的时候需要传递数据给files参数
    # 表单验证
    if form.is_valid():
        print(form.cleaned_data)
        # 上传成功需要保存数据,因为是用Form来实现,我们需要手动保存数据
        # 不能够把一个文件对象直接保存到数据库中,需要先保存这个文件对象的内容到一个文件,然后把这个文件的路径保存到数据库中
        # 1.先把图片文件保存下来,然后获取这个文件的路径,比较简单的办法就是把它保存到static/img/中,实际开发中一般保存在media文件夹里面(需要配置)
        img_obj = form.cleaned_data.get("img")
        db_file_path = os.path.join("media", img_obj.name)
        # 使用了media文件夹后,可以使得实际路径和数据库路径一样.
        img_path = db_file_path
        f = open(img_path, "wb")
        for chunk in img_obj.chunks():
            f.write(chunk)
        f.close()
        # 2.然后把这个文件的路径和姓名和年龄的数据保存到数据库中
        name = form.cleaned_data.get("name")
        age = form.cleaned_data.get("age")
        models.Boss.objects.create(name=name, age=age, img=db_file_path)
        return HttpResponse("上传成功")
    return render(req, "upload_form.html", {"form": form, "title": "利用django的Form组件实现文件上传"})  # 表单数据校验失败就会显示错误
