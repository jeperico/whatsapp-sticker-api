from django.contrib import admin
from .models import Group, Sticker


class GroupAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'description', 'created_at', 'updated_at']
  search_fields = ['name']
  list_filter = ['created_at', 'updated_at']
  readonly_fields = ['created_at', 'updated_at']

admin.site.register(Group, GroupAdmin)


class StickerAdmin(admin.ModelAdmin):
  list_display = ['id', 'image', 'description', 'created_at', 'updated_at']
  search_fields = ['description']
  list_filter = ['created_at', 'updated_at']
  readonly_fields = ['created_at', 'updated_at']

admin.site.register(Sticker, StickerAdmin)
