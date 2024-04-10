from django.urls import path, include
from rest_framework.routers import DefaultRouter
from GlenAPP.views import UserInfoViewSet

router = DefaultRouter()
router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

urlpatterns = [
]

urlpatterns += [
    path('', include(router.urls)),
]
