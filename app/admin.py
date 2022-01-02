from django.contrib import admin
from .models import Post, Result

# Post, Resultモデルを管理画面で操作
admin.site.register(Post)
admin.site.register(Result)