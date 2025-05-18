from django.conf import settings
from django.db import models
from django.utils import timezone
from .category import Category

# モデルの定義（ポスト内容をデータベースに保存する）
class Post(models.Model):
    # 属性情報（プロパティ）
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログ公開用
    def publish(self):
        if self.published_date == None:
            self.published_date = timezone.now()
        else:
            pass

        self.save()

    # ブログ非公開（下書きに戻す）用
    def unpublish(self):
        self.published_date = None
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title