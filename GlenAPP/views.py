from rest_framework.viewsets import ModelViewSet
from GlenAPP.models import UserInfo
from GlenAPP.serializer import UserInfoSerializer
from GlenAPP.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username',]
    search_fields = ('username',)
