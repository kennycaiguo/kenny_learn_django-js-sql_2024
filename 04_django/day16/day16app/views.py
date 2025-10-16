from django.http import HttpResponse
from django.shortcuts import render, redirect
from day16app.models import Department, UserInfo


# Create your views here.

def home(req):
    return HttpResponse("Welcome to the home page")


def index(req):
    return render(req, "index.html")


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
def dep_edit(req,nid):
    # 处理get
    if req.method == "GET":
        dep = Department.objects.filter(id=nid).first()
        return render(req, "dep_edit.html", {"dep": dep})
    # 处理post
    id = req.POST.get("id")
    title = req.POST.get("title")
    Department.objects.filter(id=id).update(title=title)
    return redirect("/dep/list")
