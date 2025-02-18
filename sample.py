# 必要なライブラリをインポート
from flask import Flask

# Flaskオブジェクトを生成
app = Flask(__name__)

# ルートディレクトリにアクセスしたときの処理
@app.route('/')
def hello():
    return 'Hello, World!'

# エントリーポイント
if __name__ == '__main__':
    app.run()
