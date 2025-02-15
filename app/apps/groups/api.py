from rest_framework import viewsets
from .models import Group, Sticker
from .serializers import GroupSerializer, StickerSerializer

class GroupViewSet(
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  search_fields = ['name', 'description', 'members']
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = GroupSerializer(instance)
    return Response(serializer.data)

  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = GroupSerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

  def perform_create(self, serializer):
    return super().perform_create(serializer)


class StickerViewSet(
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Group.objects.all()
  serializer_class = StickerSerializer
  search_fields = ['name', 'description', 'members']
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = StickerSerializer(instance)
    return Response(serializer.data)

  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = StickerSerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

  def perform_create(self, serializer):
    return super().perform_create(serializer)


  # group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='stickers')
  # name = models.CharField(max_length=100)
  # description = models.TextField()
  # image = models.ImageField(upload_to='stickers')
