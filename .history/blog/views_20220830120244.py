from django.shortcuts import render
from .models import Post

# ポストの一覧を表示（モデルに情報を要求し、テンプレートに渡す）
def post_list(request):
    return render(request, 'blog/post_list.html', {})