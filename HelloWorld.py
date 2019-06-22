"""
2019.06.22
对于flask来说，首先flask 需要确定本身是作为一个模块倒入还是需要运行的主模块
因此，在创建app的时候，需要把当前的模块明__name__作为参数传进来。
同时，app.run()方法可以让flask 开始创建服务器程序，同时，在run中可以指定一个白名单？
使用host=来作为一个监听的地址，如果是0.0.0.0，那么就是监听全网？（后续这个需要放到服务器上测试一下）

1。可以通过绑定的路由中指定method 来指定需要回应的方法
2。要返回一个静态的资源，需要在static（相对这个脚本的所在目录）文件夹中放置资源，然后通过url_for方法就可以返回资源
"""

from flask import Flask
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)  # 指定flask是不是运行在我们要运行的这个当前脚本中，如果是作为模块导入的，那么有可能不会执行？？


@app.route('/hello')  # 通过装饰，告诉flask什么样的URL是我应该接受处理的，当这样的URL过来的时候我就调用下面的函数
def hello_world():
    return 'Hello World!'  # 所以这个函数的返回值就是我们要传送给客户端的值？


# 这里的路由可以有很多个，不一定只有一个，比如

@app.route('/test')
def test():
    return "test"


# 动态链接，这部分的URL可能是不定的
@app.route("/test/<username>")
def testDnamicUrl(username):
    return "this is the dynamic route" + username


@app.route("/test/<path:username>")
def testDynamicTransfer(username):
    return "this is the dynamic tranfer" + username


# 重定向规则
@app.route("/test/redirect/")
def testredirect():
    return "this is the redict"


@app.route("/test/redirect")
def testRedirect():
    return "this is no slash"


@app.route("/test/request")
def dealwithRequest():
    print("the method to get html is: " + request.method)
    return redirect(url_for("testRedirect"))


# return a static resource
@app.route('/login', methods=["GET"])  # get not support
def login():
    return redirect(url_for("static", filename="HelloWorld.html"))

@app.route('/getargu',methods=["GET"])
def showArguFromGet():
    print(request.args.get("name","123"))
    print(request.args.get("this",""))
    return ""


if __name__ == "__main__":
    # host is the address which you want to bind
    # if you want public in internet,you can set this address to public address
    app.run(host="127.0.0.1", port=10000, debug=True)
