from django.contrib import admin

from blog.models import Category, Comment, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "category")
    list_filter = ("category", "tags", "status")
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)
    date_hierarchy = "created_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("nick_name", "post")
    list_filter = ("post",)
    search_fields = ("nick_name", "content")
    date_hierarchy = "created_at"
