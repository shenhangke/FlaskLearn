# 装饰器相当于在函数外面包一层函数，扩展原来函数的功能，只只不过通过python提供了一种语法糖，来简单的调用这个函数

"""
#装饰器
def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

def say_hello():
    print("hello!")

say = debug(say_hello)  # 添加功能并保持原函数名不变

#say()   #其实这里调用的是wrapper函数，在wrapper函数return部分，调用了func，返回func函数的返回值

#所以所谓的装饰器，他所修饰的函数会返回一个函数？
#但是上面的代码并没有使用到装饰器，那么我们真实的使用一下装饰器呢

@debug
def say_hello_decorate():
    print("this is the func which has deccorate by @")

say_hello_decorate():"""

"""
#所以实际上装饰器的作用就是加上了一个外层包装，让执行这个函数之前会执行一些其他已经定义好的代码
#而被装饰器修饰的函数传入的参数是一个函数指针，并且这个函数应该返回一个函数指针，这个函数可以是无预定义的

def debug_other(func):
    print("this is the direct call decorate func")
    def innerfunc():
        print("this is direct inner func")  #理论上，这里应该是要返回这个函数的，但是这里并没有返回这个函数？？？
        #或者说，函数执行到这里就报错？
        #return func()
    return innerfunc  #这里要注意的是，并没有真正的制定传进来的函数，看看是否可以执行

@debug_other
def say_hello_dir():
    print("this is the func which decorate by dir")  #这里这个函数也同时被执行了？？但是我在代码中并没有调用到这个函数啊

say_hello_dir()
#在这里报错了？为什么呢，难道得到的函数必须使用到下面的定义的函数？
#从语法上不应当做这种限制啊。。。
#解释，之前是因为innerfunc多加了一个括号，变成了执行
#这么看来，装饰器的作用就是返回一个函数，其后面修饰的函数必定会接收一个函数指针
#然后通过这个函数指针返回一个函数，这个函数可以是任意的函数，甚至可以是经过包装的函数，甚至都可以跟后面定义的函数一点关系都没有
"""
"""
    大概这个装饰器的作用就是，紧诶着的后面的函数作为一个函数指针传到修饰的函数中，然后通过这个函数返回一个函数指针。
    后面的函数名也可以当做这个装饰函数返回的函数使用
"""

"""
def debug(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        return func()  #wrapper函数返回的是外层函数传进来的函数
    return wrapper  #外层函数的返回值返回的是内部定义的这个函数

def say_hello():
    print "hello!"

say_hello = debug(say_hello)  # 添加功能并保持原函数名不变

#如果调用debug(say_hello)函数的话，实际上返回值say_hello是wrapper函数
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


# 定义一个装饰器
def docorate(func):
    print("this is the decorate start")

    def innerFunc(out: str):
        print('this is the innerfunc,the out is:' + out)

    return innerFunc


@docorate
def testOuterFunc(out: int):
    print("this is the test outer func" + out)

#这个函数要成为一个带参数的装饰，如果被@装饰的函数，后面会被马上执行（在刚刚错误传参的时候其实也验证过）
#那么利用这一点，是的最外层带参数的这个函数返回一个原来的装饰器
def arguDecorate(lever:str):
    print("the lever is: "+lever)
    def innerDecoprate(func):
        def innerFunc(innerStr:str):
            print("this is the inner func,the argu is: "+innerStr)
        return innerFunc
    return innerDecoprate


"""
分析一下这个装饰器的执行流程
1.首先，由于arguDocorate被@所装饰，并且后面传入了参数，那么这个函数就被当作一个函数，立即执行
2.上面的最外层函数被执行完之后，返回了一个参数是函数指针的函数，这个函数其实是实际上的装饰器
3.就有点类似先执行函数，然后返回一个@xxx不带参数的装饰器？
"""
@arguDecorate("log")
def testArguDeco(argu:str):
    print("this is the testout func,the argu is: "+argu)


if __name__ == '__main__':
    #由于testOuterFunc被decorate装饰
    #首先，被装饰的函数会作为装饰器的一个指针（第一个？）传入到装饰器函数中
    #然后被装饰的函数名实际上就变成了由装饰器返回的函数了
    #testArguDeco("test")
    pass
