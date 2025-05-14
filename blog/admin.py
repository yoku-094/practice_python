from django.contrib import admin
from .models import Post
from .category import Category

# Adminページ（管理画面）表示 ＝ モデルを登録する
admin.site.register(Post)
admin.site.register(Category)
