"""
URL configuration for day16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from day16 import settings
from day16app import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home),
    path('index/', views.index),
    #部门管理相关路由
    path('dep/list/', views.dep_list),
    path('dep/add/', views.dep_add),
    path('dep/del/', views.dep_del),
    # path('dep/edit/', views.dep_edit),
    # 路由格式 :http://127.0.0.1:8000/dep/1/edit
    path('dep/<int:nid>/edit/', views.dep_edit),

    # 员工管理相关路由
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/<int:nid>/edit/', views.user_edit),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
