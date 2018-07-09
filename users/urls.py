from django.conf.urls import url
from . import views

# 存放users中的全部路由
# # http://127.0.0.1:8000/users/index/
urlpatterns = [
    # 测试视图的业务逻辑
    url(r'^index/$', views.index)
]