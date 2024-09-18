from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('createdAt','updatedAt') # Specify only for reading

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('createdAt','updatedAt') # Specify only for reading

admin.site.register(Category, CategoryAdmin) 
admin.site.register(Post, PostAdmin)