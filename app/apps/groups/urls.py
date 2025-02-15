from apps.groups import api
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('sticker', api.StickerViewSet)
router.register('groups', api.GroupViewSet, basename='groups')

urlpatterns = [
  path('', include(router.urls)),
]
