from django.urls import path
from . import views

urlpatterns = [
    # 投稿一覧
    path('', views.post_list, name='post_list'),

    # 記事表示
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 新規投稿
    path('post/new/', views.post_new, name='post_new'),
]