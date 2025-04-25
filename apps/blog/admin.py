from django.contrib import admin
from .models import Post, Category
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Админ-панель модели записей
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}