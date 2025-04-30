from django.contrib import admin
from .models import Post, Category, Comment, Rating
from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

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


@admin.register(Comment)
class CommentAdminPage(DjangoMpttAdmin):
    """
    Админ-панель модели комментариев
    """
    pass



@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Админ-панель модели рейтинга
    """
    pass