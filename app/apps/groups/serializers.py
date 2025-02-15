from rest_framework import serializers
from .models import Group, Sticker

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class StickerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sticker
    fields = ['id', 'name', 'description', 'image', 'created_at', 'updated_at']
