from django.contrib import admin
from .models import *

class ItemCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Item, ItemAdmin)