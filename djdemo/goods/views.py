from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    data = "<h1>Glen Code</h1>"
    return  HttpResponse(data,content_type="text/html")

    """在视图中调用模板引擎提供的渲染函数实现前后端不分离"""
    return render()
