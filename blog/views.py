from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# ポストの一覧を表示（モデルに情報を要求し、テンプレートに渡す）
def post_list(request):
    # request：インターネットを介してユーザから受け取った全ての情報が詰まったもの
    
    # Postモデルからブログの記事を取り出して並べ替える
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # {}の中に指定した情報をテンプレートで表示（{'名前': 値（クエリセット）}）
    return render(request, 'blog/post_list.html', {'posts': posts})

# 記事詳細画面を表示
def post_detail(request, pk):
    # 404エラーページを表示
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 記事追加画面を表示
def post_new(request):
    if request.method == "POST":
        # 空のフォームを構築
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# 記事編集画面を表示
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # 構築したフォームに取得してきた内容を入れる
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})