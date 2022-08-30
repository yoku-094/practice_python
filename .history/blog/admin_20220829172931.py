from django.contrib import admin
from .models import Post

# Adminページ（管理画面）表示 ＝ モデルを登録する
admin.site.register(Post)
