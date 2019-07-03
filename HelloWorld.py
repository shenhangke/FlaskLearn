"""
2019.06.22
对于flask来说，首先flask 需要确定本身是作为一个模块倒入还是需要运行的主模块
因此，在创建app的时候，需要把当前的模块明__name__作为参数传进来。
同时，app.run()方法可以让flask 开始创建服务器程序，同时，在run中可以指定一个白名单？
使用host=来作为一个监听的地址，如果是0.0.0.0，那么就是监听全网？（后续这个需要放到服务器上测试一下）

1。可以通过绑定的路由中指定method 来指定需要回应的方法
2。要返回一个静态的资源，需要在static（相对这个脚本的所在目录）文件夹中放置资源，然后通过url_for方法就可以返回资源

使用会话之前要先设置一个密钥，这个密钥有可能是用来加密会话的？（但是会话在服务端看起来更像是明文的？）
使用会话就像是使用字典一样，直接访问即可。
当一个会话不存在的时候，直接通过session[XXX]来访问可能会爆出异常
如果要判断一个会话是不是存在，可以使用session.get()判断其返回值是不是none
"""

from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from os import path as op
from werkzeug.utils import secure_filename
from flask import session
from mysqlUtil import mysql

app = Flask(__name__)  # 指定flask是不是运行在我们要运行的这个当前脚本中，如果是作为模块导入的，那么有可能不会执行？？
app.secret_key = "shenhangke"


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
@app.route('/login_error', methods=["GET"])  # get not support
def login_error():
    return redirect(url_for("static", filename="HelloWorld.html"))


@app.route('/getargu', methods=["GET"])
def showArguFromGet():
    print(request.args.get("name", "123"))
    print(request.args.get("this", ""))
    return ""


# test the function of upload files
@app.route("/uploadFiles", methods=["POST", "GET"])
def uploadFiles():
    if request.method == "GET":
        print("this is the get methos to access upload file")
        return "hello,this is upload file function"
    print("has access the uploadFiles")
    clientFile = request.files["fileUpload"]
    if clientFile != None:
        clientFile.save(op.abspath(".") + clientFile.filename)
        print("the f.filename is: " + clientFile.filename)
        print("the secure_name is: " + secure_filename(clientFile.filename))
        return "has receive your file,thank you"


@app.route("/getHelloWorld", methods=["GET"])
def getHelloWorldSite():
    # redirect is a function to turn your request to other url
    return render_template("HelloWorld.html")


@app.route("/getJs", methods=["GET"])
def getJs():
    return redirect(url_for("static", filename="HelloWorld.js"))


@app.route("/testSession", methods=["GET"])
def testSession():
    username=request.args.get("username")
    passwd=request.args.get("passwd")
    print(username)
    print(passwd)
    session['username']=username
    session["passwd"]=passwd
    print("the session username is: "+session['username'])
    # the session just a simple key-value
    # how to save the session
    return "has connect to session"

@app.route("/sessionCon",methods=["GET"])
def testSessionConnection():
    noUser="there is no user"
    username = request.args.get("username")
    passwd = request.args.get("passwd")
    if username==session['username']:
        if passwd==session["passwd"]:
            return "connect to "+username
    return noUser

"""
    so the session is saved in memory,and it's a special key-value
    but how to persist this to database
"""


# get the session which contain username and passwd
@app.route("/session_get_user", methods=["GET"])
def getuserInfo():
    if (request.args.get("username") != "") and (request.args.get("passwd") != ""):
        database = mysql()
        mysql.insertNameAndPasswd(request.args.get("username"),
                                  request.args.get("passwd"))
        session['username']=request.args.get("username")
        session["passwd"]=request.args.get("passwd")

@app.route("/login",methods=["GET"])
def login():
    username = request.args.get("username")
    passwd = request.args.get("passwd")
    database=mysql()
    if database.queryUserInfo(username,passwd):
        # if it has queried the userinfo,create session to tract
        session[username+passwd]=username+passwd
        return "you has connect to website,and we will track you all the time"
    else:
        return "login error,please check your password and username"

@app.route("/buy",methods=["GET"])
def buy():
    username = request.args.get("username")
    passwd = request.args.get("passwd")
    #user the info to maintain session
    #print(session[username+passwd])
    if(session.get(username+passwd)!=None):
        return "you can buy something"
    else:
        return "you need login first"



if __name__ == "__main__":
    # host is the address which you want to bind
    # if you want public in internet,you can set this address to public address
    app.run(host="127.0.0.1", port=10000, debug=True)
