from apps.profiles import api
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'groups', api.GroupViewSet)
router.register(r'stickers', api.StickerViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
