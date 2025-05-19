# MyBlog

Djangoで構築したシンプルなブログアプリです。
Django学習用として[Django Girls]([http://127.0.0.1:8000](https://tutorial.djangogirls.org/ja/))を参考に作成したものに機能追加を施しました。
記事の作成・編集・公開・下書き保存など、基本的な機能を備えています。
  
  
---
  
  
## 機能一覧と実装概要
  
### 1. 記事の新規投稿・編集機能
- `edit.html` テンプレートを新規・編集で共通化
- フォームの `action` 属性を動的に指定
- 「下書き保存」「保存して公開」ボタンを設置し、POST時に `name="action"` で処理を分岐
  
  
### 2. 下書き機能
- 投稿を下書きとして保存可能
- 公開済みから下書き保存に切り替え可能
  
  
### 3. 記事の削除機能
- 管理者ログイン中は投稿詳細ページから削除可能
- 削除後に通知メッセージを表示
  
  
### 4. メッセージ機能
- `messages.success()` など Django のメッセージフレームワークを使用。
- Bootstrap のアラートと連携してメッセージ表示。
- JavaScript により、メッセージ表示後2秒で自動的にフェードアウトし非表示
  
  
### 5. 投稿のソート機能
- `sort_form.py` にて並び替え用フォームを作成。
- 投稿一覧を日付順、タイトル順などでソート可能
  
  
### 6. カテゴリ機能
- `category.py` を使用して記事にカテゴリを紐づけ
- 記事にカテゴリータグを表示
- カテゴリータグをクリックでカテゴリーごとの一覧表示
  
  
### 7. Markdown 対応
- `templatetags/markdown_filter.py` にて Markdown フィルターを作成
- 投稿本文に Markdown を記述し、テンプレートで HTML に変換して表示
- 一覧画面ではプレーンテキストに変換して表示
  
  
### 8. Bootstrap UI 適用
- ボタン、アラート、レイアウトなどのスタイルを整備
  
  
---
  
  
## セットアップ手順
  
以下の手順でローカル環境にセットアップできます。
  
### 1. 仮想環境の作成
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
  
### 2. 必要なパッケージをインストール
```bash
pip install -r requirements.txt
```
  
### 3. マイグレーション実行
```bash
python manage.py migrate
```
  
### 4. 管理者ユーザーの作成
```bash
python manage.py createsuperuser
```
  
### 5. 開発用サーバーを起動
```bash
python manage.py runserver
```
  
ブラウザで [http://127.0.0.1:8000](http://127.0.0.1:8000) にアクセスして動作確認できます。

    
---
  
  
## 使用技術
  
- Python 3.9.6
- Django 3.2.15
- SQLite3（開発用データベース）
- Bootstrap 3.2.0
- JavaScript（バツボタンや自動消去処理）
  
  
---
  
  
## ディレクトリ構成（抜粋）
  
```
.
blog/                            
├── admin.py                     # 管理画面設定
├── apps.py                      # アプリ設定
├── category.py                  # カテゴリ管理機能用モデル定義
├── forms.py                     # 投稿フォーム定義
├── models.py                    # DBモデル定義
├── sort_form.py                 # ソート用フォーム定義
├── static/                      # 静的ファイル（CSS等）
├── templates/                   # テンプレートファイル
│   └── blog/
│       ├── base.html            # 共通レイアウト
│       ├── post_detail.html     # 記事詳細ページ
│       ├── post_draft_list.html # 下書き記事一覧
│       ├── post_edit.html       # 記事編集ページ
│       └── post_list.html       # 記事一覧ページ
├── templatetags/             
│   └── markdown_filter.py       # Markdown変換用フィルター（HTML/プレーンテキスト変換）
├── urls.py                      # URLルーティング設定
└── views.py                     # 画面表示や処理を担当する関数・クラス

db.sqlite3                       # SQLiteデータベースファイル
manage.py                        # Django管理コマンド用スクリプト
mysite/                          # プロジェクト設定ディレクトリ
├── settings.py                  # プロジェクト設定（DB、アプリ等）
├── urls.py                      # プロジェクト全体のURL設定
└── wsgi.py                      # WSGI設定ファイル
myvenv/                          # Python仮想環境
node_modules/                    # フロントエンドパッケージ管理（Bootstrap等）
requirements.txt                 # Python依存パッケージリスト
```
  
  
---
  
  
## 今後の改善希望（期限未定）
  
- **タグ機能**
  - 記事に複数タグを付けられる
  
- **画像アップロード**
  - 投稿に画像を添付できる
  - 画像のサムネイル生成・管理
  
- **全文検索機能**
  - 投稿タイトルや本文を対象にした全文検索
  
- **デザイン強化**
  - レスポンシブ対応によるモバイル端末での閲覧体験向上
  
- **APIの提供**
  - REST APIを実装して外部アプリやモバイルアプリ連携
  
- **スケジューリング投稿**
  - 未来日時に自動で公開する予約投稿機能
  
- **各種アップデート**
  - Django/Pythonのバージョンアップデート対応
  - Bootstrap 4/5など新しいフレームワークへの移行
  
  
---
  
  
## ライセンス
  
MIT License（自由に利用・改変OKです）
  
  
---
