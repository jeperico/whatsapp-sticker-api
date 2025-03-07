from django.db import models
from utils.models import BaseModel
import base64
from django.core.files.base import ContentFile


class Group(BaseModel):
  name = models.CharField(max_length=100)
  description = models.TextField()
  # members = models.ManyToManyField(User, related_name='groups')

  def __str__(self):
    return self.name


class Sticker(BaseModel):
  # group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='stickers')
  description = models.TextField()
  image = models.CharField()

  def __str__(self):
    return self.name
