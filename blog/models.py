from django.conf import settings
from django.db import models
from django.utils import timezone


# モデルの定義（ポスト内容をデータベースに保存する）
class Post(models.Model):
    # 属性情報（プロパティ）
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログ公開用メソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title