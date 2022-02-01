from unicodedata import category
from django.contrib import admin
from .models import Post, Categories

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'created_at']
    list_filter = ('created_at',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug']


