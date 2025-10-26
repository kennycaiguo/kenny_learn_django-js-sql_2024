from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class Middleware1(MiddlewareMixin):
    """中间件1"""

    def process_request(self, req):
        print("进入中间件1....")
        return HttpResponse("无权访问!!!")

    def process_reponse(self, req, res):
        print("从中间件1出来....")
        return res


class Middleware2(MiddlewareMixin):
    """中间件2"""

    def process_request(self, req):
        print("进入中间件2....")

    def process_reponse(self, req, res):
        print("从中间件2出来....")
        return res
