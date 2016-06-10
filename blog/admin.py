from django.contrib import admin

# Register your models here.

from .models import Post # . 의 의미는 현재 위치
from .models import Comment
from .models import Category


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)