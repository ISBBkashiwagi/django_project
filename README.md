# Djangoプロジェクト

# 見るべきディレクトリ・ファイル
アプリの処理が書いてあるpyファイルは、以下のディレクトリに存在しております
  ・django_project/learning_users/basic_app/　（model層とcontroller層）
  ・django_project/learning_users/templates/basic_app/　（view層）
   
#各pyファイルが何をしているのかざっくり説明
・ urls.py :　クライアント側のHttpリクエストに応じて、どのviewを実行するのか定義する
・ views.py :　urls.pyから呼び出されて、Model（データ）とView（テンプレート）を結び付けてクライアント側に返却する
・ models.py : Model(データ)を扱う部分で、主にテーブルの定義を行う
・ forms.py : model.pyで定義されたテーブルをもとに、入力フォームを部品化する


