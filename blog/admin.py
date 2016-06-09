from django.contrib import admin

from .models import Post
from .models import Comment
from .models import Tag
from .models import Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)

