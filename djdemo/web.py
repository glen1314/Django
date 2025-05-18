from flask import Flask

app = Flask(__name__)

#创建了网址/show/info 和函数index的对应关系，之后用户访问该地址，网站自动执行index
@app.route("/show/info")
def index():
    return '中国联通'

if __name__ == '__main__':
    app.run()