from rest_framework.viewsets import ModelViewSet
from GlenAPP.models import UserInfo
from GlenAPP.serializer import UserInfoSerializer
from GlenAPP.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from random import sample
from django.shortcuts import render


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username',]
    search_fields = ('username',)

def index(request):
    return HttpResponse("Hello,world.You are at the polls index Glen")

def home(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits,3)
    return render(request,'index.html',{'fruits': selected_fruits})

def detail(request,question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(request,question_id):
    response = "You are looing at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s" % question_id)
