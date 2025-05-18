from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from .models import Post
from .models import Category
from .forms import PostForm
from .sort_form import SortForm
from django.core.paginator import Paginator
from django.contrib import messages

# 公開記事一覧表示
def post_list(request, category_id=None):
    form = SortForm(request.GET)
    sort_values = '-created_date'
    # ソート機能
    if form.is_valid():
        sort_values = form.cleaned_data.get('sort') or sort_values

    category_type = None
    if category_id:
        # カテゴリーで絞る場合
        category_type = get_object_or_404(Category, pk=category_id)
        posts = Post.objects.filter(published_date__lte=timezone.now(), category=category_type).order_by(sort_values)
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(sort_values)

    # ページネーション
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    show_pagination = True
    
    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'form': form,
        'category_type': category_type,
        'show_pagination':show_pagination
    })

# 記事詳細画面を表示
def post_detail(request, pk):
    # 404エラーページを表示
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {
        'post': post
    })

# 記事追加画面を表示
def post_new(request):
    show_pagination = False

    if request.method == "POST":
        action = request.POST.get('action')
        if action not in ['save_draft', 'publish']:
            messages.error(request, "無効な操作です。")
            return redirect('post_list')

        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            if action == 'publish':
                post.publish() 
                messages.success(request, "記事を公開しました。")
                return redirect('post_list')
            else :
                messages.success(request, "記事を下書きとして保存しました。")
                return redirect('post_draft_list')
        else:
            messages.error(request, "フォームの入力内容に誤りがあります。")
            return redirect('post_list')
    else:
        # 新規作成の場合は空のフォーム
        form = PostForm()

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'form_action_url': reverse('post_new'),
        'show_pagination':show_pagination
    })

# 記事編集画面を表示
def post_edit(request, pk):
    show_pagination = False

    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        action = request.POST.get('action')
        if action not in ['save_draft', 'publish']:
            messages.error(request, "無効な操作です。")
            return redirect('post_list')
        
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            if action == 'publish':
                post.publish() 
                messages.success(request, "記事を公開しました。")
                return redirect('post_detail', pk=post.pk)
            else :
                post.unpublish() 
                messages.success(request, "記事を下書きとして保存しました。")
                return redirect('post_draft_list')
        else:
            messages.error(request, "フォームの入力内容に誤りがあります。")
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'form_action_url': reverse('post_edit', args=[pk]),
        'show_pagination':show_pagination
    })

# 下書き一覧を表示
def post_draft_list(request):
    show_pagination = False

    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')

    return render(request, 'blog/post_draft_list.html', {
        'posts': posts,
        'show_pagination':show_pagination
    })

# 下書きを公開
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.publish()
        messages.success(request, "記事を公開しました。")

    return redirect('post_detail', pk=pk)

# 記事を削除
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "記事を削除しました。")

    return redirect('post_list')
