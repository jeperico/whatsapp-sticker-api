from apps.groups import api
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('groups', api.GroupViewSet)
router.register('stickers', api.StickerViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
