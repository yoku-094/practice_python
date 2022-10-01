from django.urls import path
from . import views

urlpatterns = [
    # 投稿一覧
    path('', views.post_list, name='post_list'),

    # 記事表示
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 新規投稿
    path('post/new/', views.post_new, name='post_new'),

    # 編集
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # 草稿一覧
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # 記事掲載
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),

    # 記事削除
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]