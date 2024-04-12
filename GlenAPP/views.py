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
