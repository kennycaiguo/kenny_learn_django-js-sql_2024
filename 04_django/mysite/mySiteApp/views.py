from django.shortcuts import render,redirect
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


def tpl(req):
    jobs = ["管理员", "司机", "保安"]
    isGood = True
    jack = {
        "name": "Jack",
        "age": 19,
        "gender": "male"
    }
    users = [
        {"id": "u001", "name": "Mary", "gender": "Female", "age": 20},
        {"id": "u002", "name": "Ron", "gender": "Male", "age": 21},
        {"id": "u003", "name": "Magret", "gender": "Female", "age": 22},
    ]
    return render(req, "tpl.html",
                  {
                      'msg': "Hello Django Template!!!",
                      'jobs': jobs,
                      "state": isGood,
                      "person": jack,
                      "users": users
                  })


def movies(req):
    import requests
    from bs4 import BeautifulSoup

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
    url = "https://movie.douban.com/top250"
    # 这里只是爬取一页
    sub_url = url + f"?start=0"
    res = reps = requests.get(sub_url, headers=headers).text
    # print(reps.text)

    soup = BeautifulSoup(res, "html.parser")
    # print(soup)

    titles = soup.findAll("span", attrs={"class": "title"})
    bds = soup.findAll("div", attrs={"class": "bd"})
    chinese_titles = []
    summ = []
    for bd in bds:
        # print(bd.p.text)
        summ.append(bd.p.text)
    for title in titles:
        # print(title.string) # 不要标签,只需要标签里面的内容
        # if not title.string.__contains__("/"):  # 过滤掉英文标题,注意到英文标题都是以 / 开头  ok
        # if title.string.find("/")==-1:  # 过滤掉英文标题,注意到英文标题都是以 / 开头  ok,find方法找到了返回一个不是负数的结果,-1表示找不到,我们这里就需要它找不到
        if "/" not in title.string:  # 过滤掉英文标题,注意到英文标题都是以 / 开头 也是ok的
            chinese_titles.append(title.string)
            # print(title.string)
    summ.pop(0)
    # print(summ)
    # print(chinese_titles)
    movies = dict(zip(chinese_titles, summ))
    print(movies)
    return render(req, "movies.html", {"movies": movies})


def reqTest(req):
    print(req)
    # 获取请求方式
    print(req.method)
    print(req.body) # post请求发送过来的数据 # 这里是空,因为这是get请求
    print(req.user) # AnonymousUser
    print(req.headers)
    print(req.session)
    print(req.path)
    print(req.META)
    print(req.GET) #可以获取get请求参数
    print(req.POST) #可以获取post请求数据

    # return HttpResponse("服务器返回的数据")
    return redirect("/userlist")



def login(req):
    if req.method=="GET":
        return render(req,"login.html")
    else:
        # post请求,需要获取用户信息
        print(req.POST)
        return HttpResponse("登录成功")
