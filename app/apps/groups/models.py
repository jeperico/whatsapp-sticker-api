from django.db import models
from utils.models import BaseModel


class Group(BaseModel):
  name = models.CharField(max_length=100)
  description = models.TextField()
  members = models.ManyToManyField('users.User', related_name='groups')

  def __str__(self):
    return self.name


class Sticker(BaseModel):
  group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='stickers')
  name = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to='stickers')

  def __str__(self):
    return self.name
