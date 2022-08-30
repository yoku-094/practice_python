from django.shortcuts import render
from django.utils import timezone
from .models import Post

# ポストの一覧を表示（モデルに情報を要求し、テンプレートに渡す）
def post_list(request):
    # request：インターネットを介してユーザから受け取った全ての情報が詰まったもの
    
    # Postモデルからブログの記事を取り出して並べ替える
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # {}の中に指定した情報をテンプレートで表示（{'名前': 値（クエリセット）}）
    return render(request, 'blog/post_list.html', {'posts': posts})