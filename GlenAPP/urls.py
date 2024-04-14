from django.urls import path, include
from rest_framework.routers import DefaultRouter
from GlenAPP.views import UserInfoViewSet
from django.urls import re_path as url
from django.contrib import admin
from GlenAPP import views


router = DefaultRouter()
router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

urlpatterns = [
    # url(r'^$',views.home,name='home'),
    # url(r'^admin/',admin.site.urls),
    path("",views.index,name="index"),
    # /GlenAPP/5/
    path("<int:question_id>/",views.detail,name="detail"),
    # /GlenAPP/5/results/
    path("<int:question_id>/results/",views.results,name="results"),
    # /Glen/5/vote/
    path("<int:question_id>/vote/",views.vote,name="vote"),


]

urlpatterns += [
    path('', include(router.urls)),
]
