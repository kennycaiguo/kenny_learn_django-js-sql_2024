from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    print(request)
    return HttpResponse("Welcome to index of mysite...")


def home(req):
    print(req)
    return HttpResponse('<h1>This is the home page</h1>')


def user_list(req):
    return render(req, "userlist.html")


def register(req):
    return render(req, "register.html")
