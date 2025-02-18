# coding:utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # DBから以下の変数を読み込んできたと仮定
    title_= "ようこそ"
    message_ = "MTVデザインパターンでWebアプリ作成"

    return render_template("index.html", title=title_, message=message_)

# エントリーポイント
if __name__ == '__main__':
    app.run()