from django.contrib import admin

from .models import *

class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'title', 'writer', 'regdate']
    list_display_links =  ['post_id', 'title']
    ordering = ['-post_id']
    inlines = [CommentInlineAdmin]
    search_fields = ['writer', 'title']
    list_filter = ['fk_category_id']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'writer', 'memo', 'regdate']
    list_display_links =  ['comment_id']
    ordering = ['-comment_id']
    search_fields = ['writer']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)