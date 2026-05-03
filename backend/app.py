from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 连接数据库 — 注意密码替换成你实际设置的密码
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:whp@whp920@localhost/shunjing_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello, Flask! 数据库已连接'

if __name__ == '__main__':
    app.run(debug=True, port=5000)