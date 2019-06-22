# Djangoプロジェクト

## 見るべきディレクトリ・ファイル
アプリの処理が書いてあるpyファイルは、以下のディレクトリに存在しております
- django_project/learning_users/basic_app/　（model層とcontroller層）
- django_project/learning_users/templates/basic_app/　（view層）
   
## 各pyファイルが何をしているのかざっくり説明
### django_project/learning_users/basic_app/配下
- urls.py :　クライアント側のHttpリクエストに応じて、どのviewを実行するのか定義する
- views.py :　urls.pyから呼び出されて、Model（データ）とView（テンプレート）を結び付けてクライアント側に返却する
- models.py : Model(データ)を扱う部分で、主にテーブルの定義を行う
- forms.py : model.pyで定義されたテーブルをもとに、入力フォームを部品化する
### django_project/learning_users/basic_app/配下
- base.html ：今回のWebアプリの画面の共通部分（ヘッダー）のhtml
- index.html :トップ画面
- registration.html : ユーザー登録画面
- login.html :ログイン画面
- micropost.html :短い記事を投稿する画面
- post_edit.html :短い記事を編集する画面
- posts.html : 記事一覧画面（ページング処理は未実装）
